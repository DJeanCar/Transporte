from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)


SECRET_KEY = '4+jlejsf8yn2040eq)zx=1&=6e!4+q6fvlb$rp4j^i6_#n(@z-'

LOCAL_APPS = (
		'apps.home',
		'apps.users',
	)

THIRD_PARTY_APPS = (

	)

DJANGO_APPS = (
		'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	)

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Transporte.urls'
WSGI_APPLICATION = 'Transporte.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]
