from django.urls import path


from logger.views import LogsView, IpLogListView


app_name = 'logger'

urlpatterns = [
    path('logs/', LogsView.as_view(), name='logs'),
    path('ip-logs/', IpLogListView.as_view(), name='ip-logs'),
]
