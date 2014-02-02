# Django settings for lorem project.
import os, sys
DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))+'/..'
print PROJECT_ROOT
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
ACCOUNT_ACTIVATION_DAYS = 3

#TUHES_BASKET_ITEM_APP = 'catalog'
#TUHES_BASKET_ITEM_MODEL = 'item'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'siskopedia',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []
TIME_ZONE = 'Asia/Irkutsk'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = PROJECT_ROOT+'/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_ROOT+'/staticroot/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
        PROJECT_ROOT+"/static/",
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = 'ioa#y33heig+a+kl$3@j@3ft0$w9o4u8_2d3i3=*u=c(=ckln%'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS =(
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
	)

ROOT_URLCONF = 'lorem.urls'
WSGI_APPLICATION = 'lorem.wsgi.application'

TEMPLATE_DIRS = (
	PROJECT_ROOT+'/templates/',
)

INSTALLED_APPS = (
    	'django.contrib.auth',
   	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	'django.contrib.sites',
    	'django.contrib.messages',
    	'django.contrib.staticfiles',
    	'django.contrib.admin',
    	#'haystack',
    	#'mptt',
	'django_thumbs',
	'autoslug',
	'users',
	'registration',
	'catalog',
	#'slider',
	'pages',
	#'tuhes_basket',
	'tuhes_breadcrumbs',
	
	#'basket',
	#'feedback',
	#'profiles',
	'tags',
	'grappelli',
	'filebrowser',
    # Uncomment the next line to enable the admin:
    	
    # Uncomment the next line to enable admin documentation:
    	'django.contrib.admindocs',
    #	'grappelli',
	'foundation',    
	'south',
        'menuz',
		
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

AVAILABLE_MENUS = (
	{
		'id': 'top_menu',
		'title': ('Top Menu'),
		'type': 'UL',          #optional, default UL. alternative 'OL'
		'class': 'someclass',  #optional, output: <ul class="ul_toplevel someclass">
		'before_link': 'BBB',  #optional, can be text or html tag. output: <li>BBB<a href="...">Title</a></li>
		'after_link': 'AAA',   #optional, can be text or html tag. output: <li><a href="...">Title</a>AAA</li>
	},
)
