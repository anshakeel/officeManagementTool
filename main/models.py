from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
u = User.objects.filter(is_staff=True)
from django.conf import settings
User = get_user_model()
# Create your models here.
class worker(models.Model):
    Worker = models.ForeignKey(User, limit_choices_to={'is_staff': False},on_delete=models.CASCADE)
    WorkType = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000,blank=True)
    comment = models.CharField(max_length=1000,blank=True,null=True)
    image = models.ImageField(upload_to='pics',blank=True)
    file = models.FileField(upload_to='router_specifications')
    #Completion_Time = models.TimeField(_(u"Conversation Time"), auto_now_add=False, blank=True)
    Client_Name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    Urgent = models.BooleanField(default=False)
    progress = models.IntegerField(default=0,blank=True,null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
      return f'{self.Worker}'

class completeTask(models.Model):
    task = models.ForeignKey(worker, on_delete=models.CASCADE, related_name='+')
    aboutTask = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='completedPics')
    file = models.FileField(upload_to='completed')
    # Completion_Time = models.TimeField(_(u"Conversation Time"), auto_now_add=False, blank=True)
    Client_Name = models.CharField(max_length=100)


class Announce(models.Model):
    accouncement = models.CharField(max_length=1000)