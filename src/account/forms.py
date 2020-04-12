from django import forms
from django.core.exceptions import ValidationError


from account.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2', 'birth_date', 'phone')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords do not match!')

        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise ValidationError(f'Phone number {phone} consists not only from digits. '
                                  f'It should be introduced like this example: 123456789')

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.save()
        return user
