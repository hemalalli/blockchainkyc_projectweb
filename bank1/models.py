from django.db import models
from fileupload.models import User_Profile
# Create your models here.

class ipfsmapping(models.Model):
    ipfsid = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    userid = models.ForeignKey("fileupload.User_Profile", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.userid)
