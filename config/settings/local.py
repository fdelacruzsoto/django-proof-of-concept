from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='&hpd^*9vj=^+_p5y-iufb8czel)m+7bah_4)2!o(0j%no5^q=t')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
