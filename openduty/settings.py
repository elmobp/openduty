# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType
djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

BROKER_URL = 'django://'

LOGIN_URL = '/login/'

PROFILE_MODULE = 'openduty.UserProfile'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'kombu.transport.django',
    'openduty',
    'openduty.templatetags',
    'schedule',
    'djcelery',
    'notification',
    'django_tables2',
    'django_tables2_simplefilter',
    'bootstrap3',
    "django_twilio",
    "django_saml2_auth"
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'openduty.urls'

WSGI_APPLICATION = 'openduty.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIRST_DAY_OF_WEEK = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 10
}

PAGINATION_DEFAULT_PAGINATION = 20 # The default amount of items to show on a page if no number is specified.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT =  os.path.realpath(os.path.dirname(__file__))+"/static/"
STATICFILES_DIRS = (
    os.path.realpath(os.path.dirname(__file__))+'/static_schedule/',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

AUTH_PROFILE_MODULE = 'openduty.UserProfile'

BASE_URL = os.environ["BASE_URL"]

XMPP_SETTINGS = {
}

EMAIL_SETTINGS = {
    'host': os.environ["SMTP_HOST"],
    'from': os.environ["SMTP_FROM"],
}

SLACK_SETTINGS = {
   'apikey': os.environ["SLACK_KEY"]
}

SERVICENOW_ENABLED = True

SERVICENOW_SETTINGS = {
   'instance': os.environ["SN_INSTANCE"],
   'username': os.environ["SN_USERNAME"],
   'password': os.environ["SN_PASSWORD"],
   'caller_id': os.environ["SN_CALLER_ID"],
   'contact_type': os.environ["SN_CONTACT_TYPE"],
}

SERVICENOW_CUSTOM_FIELDS = {
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_sqlite.db',
    }
}

PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
)
ALLOWED_HOSTS='*'

TWILIO_SETTINGS = {
    'SID': os.environ["TWILIO_ACCOUNT_SID"],
    'token': os.environ["TWILIO_AUTH_TOKEN"],
    'sms_number': os.environ["TWILIO_SMS"],
    "phone_number": os.environ["TWILIO_PHONE"],
}

SAML_USE_NAME_ID_AS_USERNAME = True

# urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
SAML2_AUTH = {
    # Required setting
    'SAML_CLIENT_SETTINGS': { # Pysaml2 Saml client settings (https://pysaml2.readthedocs.io/en/latest/howto/config.html)
        'entityid': 'https://URL-TO-OD/saml2_auth/acs/', # The optional entity ID string to be passed in the 'Issuer' element of authn request, if required by the IDP.
        'metadata': {
            'local': [
                   "/opt/openduty/openduty/metadata.xml"
            ],
        },
       'service': {
         'sp': {
          'name_id_format': 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified'
        }
       },
'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'Email',
        'username': 'UserName',
        'first_name': 'FirstName',
        'last_name': 'LastName',
    }
    },
}
