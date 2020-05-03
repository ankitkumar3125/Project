from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.IntegerField()
    Real_Name=models.CharField(max_length=25)
    Time_zone = models.CharField(max_length=100)
    def __str__(self):
        return self.Real_Name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aid = models.IntegerField()
    Start_Time= models.DateTimeField()
    End_Time = models.DateTimeField()


