import datetime


from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


from account.models import User
from account.forms import SignUpForm, EditProfileForm
from logger.models import IpLogger


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class EditProfileView(UpdateView):
    template_name = 'edit_profile.html'
    queryset = User.objects.filter(is_active=True)
    success_url = reverse_lazy('index')
    form_class = EditProfileForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)

    def get_success_url(self):
        with open('IP.txt', 'a') as file:
            ip = get_client_ip(self.request)
            file.write(
                f'Profile with id: {self.request.user.id} is changed. '
                f'IP address: {ip}. '
                f'Time: {datetime.datetime.now()}. \n'
            )
        IpLogger.objects.create(
            user_ip=ip,
            changed_id=self.request.user.id
        )
        return super().get_success_url()
