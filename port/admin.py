from django.contrib import admin
from .models import contact, project
# Register your models here.
admin.site.register((project,contact))