from django.urls import path


from logger.views import LogsView


app_name = 'logger'

urlpatterns = [
    path('logs/', LogsView.as_view(), name='logs'),
]


