from django.views.generic import CreateView
from django.urls import reverse_lazy


from account.models import User
from account.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm
