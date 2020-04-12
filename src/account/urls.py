from django.urls import path


from account.views import SignUpView, EditProfileView


app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit-profile/<int:pk>', EditProfileView.as_view(), name='edit-profile'),
]


