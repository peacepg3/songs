# from django.contrib import admin
# from .models import pgattribute
# # Register your models here.
# admin.site.register(pgattribute)

from django.contrib import admin
from .models import *

# Register your models here.

class song_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug_field':('song_model',)}
admin.site.register(songmodel,song_Admin)


class detail_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug_field':('song_name',)}
    list_display = ['song_name','song_id']
admin.site.register(song_details,detail_Admin)
