from django.views.generic.list import ListView


from logger.models import Logger


class LogsView(ListView):
    model = Logger
    template_name = 'logs_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Logger.objects.all()
        context['logs'] = queryset
        return context
