from django.db import models

# Create your models here.

class User_Profile(models.Model):
    kycid = models.CharField(max_length=200,unique=True)
    fname = models.CharField(max_length=200)
    email = models.EmailField(default=None)
    display_picture = models.FileField(upload_to = 'uploads/')

    def __str__(self):
        return self.kycid


class files_upload(models.Model):
    filetype = models.CharField(max_length=200)
    filename = models.FileField(upload_to = 'uploads/')
    fileid = models.ForeignKey("User_Profile", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fileid)

class status(models.Model):
    uid = models.ForeignKey("User_Profile", on_delete=models.CASCADE,unique=True)
    status = models.CharField(max_length=200, default=None)

    def __str__(self):
        return str(self.uid)

class notifications(models.Model):
    nuid = models.ForeignKey("User_Profile", on_delete=models.CASCADE,unique=True)
    notify = models.CharField(max_length=800, default=None)
    approvestatus = models.CharField(max_length=200, default=None)

    def __str__(self):
        return str(self.nuid)