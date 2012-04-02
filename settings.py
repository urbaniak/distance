import os


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

MANAGERS = ADMINS = (
)

DEBUG = True

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-GB'

SITE_ID = 1

USE_I18N = False
USE_L10N = False
USE_TZ = False

ROOT_URLCONF = 'urls'

LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
		os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
)

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
	'django.contrib.contenttypes',
	'django.contrib.staticfiles',
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': [],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

local_settings = os.path.join(PROJECT_ROOT, 'local_settings.py')
if os.path.isfile(local_settings):
	execfile(local_settings)
