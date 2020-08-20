from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import  Image



class officeId(models.Model):
    identification = models.CharField(max_length=20)
    username = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(null=True , blank= True)
    address = models.CharField(blank=True ,max_length=100)
    bio = models.CharField(blank=True,max_length=1000)
    img = models.ImageField(default='user.png',upload_to= "pics")
    exp = models.CharField(blank=True,max_length=1000)
    age = models.IntegerField(null=True , blank= True)
    join_date = models.DateField(default=datetime.date.today)
    dob = models.DateField(default=datetime.date.today)

    def __str__(self):
      return f'{self.user}Profile'


    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


        Img = Image.open(self.img.path)

        if Img.height >600  or Img.width > 600:
            output_size = (600,600)
            Img.thumbnail(output_size)
            Img.save(self.img.path)

