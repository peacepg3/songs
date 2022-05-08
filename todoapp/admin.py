from django.contrib import admin

# Register your models here.
from . models import todomodel
admin.site.register(todomodel)
