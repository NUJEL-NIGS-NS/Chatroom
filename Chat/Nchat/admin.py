from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display=['id','content','timetamp','group']

admin.site.register(Group)
