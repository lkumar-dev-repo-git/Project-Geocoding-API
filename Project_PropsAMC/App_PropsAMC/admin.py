from django.contrib import admin

# Register your models here.

from .models import UploadFilesDB

#admin.site.register(UploadFilesDB)

@admin.register(UploadFilesDB)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'date_of_uploaded')