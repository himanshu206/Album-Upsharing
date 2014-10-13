
from django.db import models

# Create your models here.


class saveRegister(models.Model):
    f_name = models.CharField(max_length=256)
    l_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    def __unicode__(self):
        return self.f_name



class AlbumInfo(models.Model):
    user = models.ForeignKey(saveRegister)
    albumName = models.CharField(max_length=256)
    date = models.DateField()
    count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.albumName



class AlbumPhotos(models.Model):
    albumPhoto = models.ForeignKey(AlbumInfo)
    photo = models.ImageField(upload_to="user_images/")
    def __unicode__(self):
        return self.photo

