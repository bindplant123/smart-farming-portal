import os
import django
from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartfarmingportal.settings')
django.setup()

try:
    print(f"set_language: {reverse('set_language')}")
except Exception as e:
    print(f"set_language error: {e}")

try:
    print(f"django.conf.urls.i18n.set_language: {reverse('django.conf.urls.i18n.set_language')}")
except Exception as e:
    print(f"django.conf.urls.i18n.set_language error: {e}")
