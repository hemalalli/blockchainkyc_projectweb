from django.contrib import admin
from django.db import models
from .models import User_Profile, status, files_upload, notifications

admin.site.register(User_Profile)
admin.site.register(status)
admin.site.register(files_upload)
admin.site.register(notifications)