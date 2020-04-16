from django.urls import path


from logger.views import LogsView, IpLogListView, ChangeLogListView


app_name = 'logger'

urlpatterns = [
    path('logs/', LogsView.as_view(), name='logs'),
    path('ip-logs/', IpLogListView.as_view(), name='ip-logs'),
    path('change-logs/', ChangeLogListView.as_view(), name='change-logs'),
]
