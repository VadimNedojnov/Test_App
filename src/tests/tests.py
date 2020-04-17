import pytest
from django.core.exceptions import ValidationError
from faker import Faker


from django.urls import reverse


from account.models import User
from account.views import get_client_ip, EditProfileView
from account.forms import SignUpForm, EditProfileForm


FAKE = Faker()


def test_sanity():
    assert 200 == 200


@pytest.mark.django_db
def test_index_page(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logs_page(client):
    url = reverse('logger:logs')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_profile_page(client):
    User.objects.create(
        email=FAKE.email(),
        phone=''.join(i for i in FAKE.phone_number() if i.isdigit()),
    )
    user = User.objects.last()
    url = reverse('account:edit-profile', kwargs={'pk': user.id})
    response = client.get(url)
    print(response.context)
    assert response.status_code == 404
    User.objects.all().delete()


@pytest.mark.django_db
def test_user_create():
    email = FAKE.email()
    phone = FAKE.phone_number()
    User.objects.create(
        email=email,
        phone=''.join(i for i in phone if i.isdigit()),
    )
    assert User.objects.all().count() == 1
    user = User.objects.last()
    assert user.phone == ''.join(i for i in phone if i.isdigit())
    assert user.email == email
    User.objects.all().delete()


class RequestA:
    META = {
        'HTTP_X_FORWARDED_FOR': '1',
    }


class IdMock:
    id = -1   # For understanding in logs that this is a test user


class RequestB:
    META = {
        'REMOTE_ADDR': '127.0.0.1'
    }
    user = IdMock


def test_get_client_ip():
    ip_a = get_client_ip(RequestA)
    assert ip_a == '1'
    ip_b = get_client_ip(RequestB)
    assert ip_b == '127.0.0.1'


class MockObject:
    __dict__ = []


@pytest.mark.django_db
def test_edit_profile_view():
    fake_object = EditProfileView()
    fake_object.request = RequestB
    fake_object.object = MockObject
    fake_object.get_success_url()


@pytest.mark.django_db
def test_sign_up_form_clear():
    form = SignUpForm()
    form.cleaned_data = {
        'password': 'password',
        'password2': 'password',
        'phone': ''.join(i for i in FAKE.phone_number() if i.isdigit())[:10]
    }
    form.clean()
    form.save()


@pytest.mark.django_db
def test_sign_up_form_not_clear():
    form = SignUpForm()
    form.errors['fake_error'] = 'fake'
    form.cleaned_data = {
        'password': 'password',
        'password2': 'password',
        'phone': ''.join(i for i in FAKE.phone_number() if i.isdigit())[:10]
    }
    form.clean()
    form.errors.pop('fake_error')


def test_sign_up_form_wrong_password2():
    form = SignUpForm()
    form.cleaned_data = {
        'password': 'password',
        'password2': 'password2',
        'phone': ''.join(i for i in FAKE.phone_number() if i.isdigit())[:10]
    }
    try:
        form.clean()
    except ValidationError:
        pass
    else:
        assert 2 == 1


def test_sign_up_form_wrong_phone():
    form = SignUpForm()
    form.cleaned_data = {
        'password': 'password',
        'password2': 'password',
        'phone': FAKE.phone_number()
    }
    try:
        form.clean()
    except ValidationError:
        pass
    else:
        assert 2 == 1


def test_sign_up_form_to_short_phone():
    form = SignUpForm()
    form.cleaned_data = {
        'password': 'password',
        'password2': 'password',
        'phone': '2'
    }
    try:
        form.clean()
    except ValidationError:
        pass
    else:
        assert 2 == 1


def test_edit_profile_form():
    form = EditProfileForm()
    form.cleaned_data = {
        'phone': ''.join(i for i in FAKE.phone_number() if i.isdigit())[:10]
    }
    form.clean()


def test_edit_profile_form_phone_not_isdigit():
    form = EditProfileForm()
    form.cleaned_data = {
        'phone': FAKE.phone_number()[:10]
    }
    try:
        form.clean()
    except ValidationError:
        pass
    else:
        assert 2 == 1


def test_edit_profile_form_phone_to_short():
    form = EditProfileForm()
    form.cleaned_data = {
        'phone': '2'
    }
    try:
        form.clean()
    except ValidationError:
        pass
    else:
        assert 2 == 1


def test_apps_files():
    import account.apps
    import logger.apps
    import test_app.wsgi
