from django.contrib import admin
from .models import userinfo, file_upload

# Register your models here.
admin.site.register(userinfo),
admin.site.register(file_upload)
