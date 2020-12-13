from django.db import models

# Create your models here.

class UploadFilesDB(models.Model):
    title = models.CharField(max_length=30)
    file_name = models.FileField()
    date_of_uploaded = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title