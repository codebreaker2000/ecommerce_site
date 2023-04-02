from ecomsite.settings import *
from decouple import config
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['ecommercesite-production.up.railway.app']