# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'as3(&&(@yre&@0)li6oyn8-i0*bk^5(t-=r6yrz5i_=bb4ge^d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'YourEmailAddress'
EMAIL_HOST_PASSWORD = 'YourEmailPassword'
