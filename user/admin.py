from django.contrib import admin
from user.models import Account, MealSetting

# Register your models here.
# Pending task need to do https://realpython.com/customize-django-admin-python/
admin.site.register(Account)
admin.site.register(MealSetting)