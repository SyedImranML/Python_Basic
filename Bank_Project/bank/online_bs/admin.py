from django.contrib import admin

# Register your models here.

from .models import Register
from .models import Transaction

admin.site.register(Register)
admin.site.register(Transaction)


#python manage.py makemigrations
#python manage.py  migrate

