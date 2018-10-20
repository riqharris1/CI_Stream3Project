from settings.base import *
import os
import settings
import dj_database_url



DEBUG = True

# Load the ClearDB connection details from the environment variable
#DATABASES['default'] =  dj_database_url.config()
DATABASES = {
    'default': {
        #'default': dj_database_url.config('DATABASE_URL'),
        'default': dj_database_url.config('CLEARDB_IVORY_URL'),
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
        
    }
}    
    
''' 
#DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR ,'db.sqlite3'),
    'default': dj_database_url.config('CLEARDB_DATABASE_URL'),
    }
} '''
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_nbWefqblVg8HnYsFmpcld8qj')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_N35jP51CRqW4FKBMa8MAL1A4')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://ci-stream3project.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'rickharrisIT@gmx.com'

SITE_URL = 'https://ci-stream3project.herokuapp.com/'
#ALLOWED_HOSTS.append('ci-stream3project.herokuapp.com')
ALLOWED_HOSTS.append('ci-stream3project-rickharris.herokuapp.com')
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
