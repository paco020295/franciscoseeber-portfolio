from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()


class Competence(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=False, null=False, storage=gd_storage)

    def __str__(self):
        return self.title
