import datetime


from django import forms
from django.core.exceptions import ValidationError


from account.models import User


this_year = datetime.date.today().year
years = range(this_year - 120, this_year)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

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
        if len(phone) < 9 or len(phone) > 12:
            raise ValidationError(f'Phone number {phone} is not valid!')
        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.save()
        return user


class EditProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'email',
            'phone',
            'biography',
            'linkedin_link',
            'githab_link',
            'twitter_link',
            'facebook_link',
        )

    def clean(self):
        cleaned_data = super().clean()

        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise ValidationError(f'Phone number {phone} consists not only from digits. '
                                  f'It should be introduced like this example: 123456789')
        if len(phone) < 9 or len(phone) > 12:
            raise ValidationError(f'Phone number {phone} is not valid!')
        return cleaned_data
