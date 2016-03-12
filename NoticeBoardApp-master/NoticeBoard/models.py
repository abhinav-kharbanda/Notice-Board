from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
# Create your models here.
class Notice(models.Model):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    priority_value = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High')
    )
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, blank=True)
    display_title= models.BooleanField()
    publish_date = models.DateField('Date Published')
    expiry_date = models.DateField('Expiry Date')
    content = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to="Pictures", blank=True)
    sign_image = models.ImageField(upload_to="Pictures/Sign", blank=True)
    video = models.FileField(upload_to='videos/', blank=True, help_text="Upload only .mp4 videos")
    display_video = models.BooleanField()
#   priority = models.IntegerField(default=HIGH, choices=priority_value)
    def __unicode__(self):
        return self.title
    def is_expired(self):
        if date.today()>self.expiry_date:
            return True
        else:
            return False
            
   
#   def priority_ret(self):
#    	return self.priority
class News(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField('Date Published')
    expiry_date = models.DateField('Expiry Date')
    class Meta:
        verbose_name_plural = "News"
    def __unicode__(self):
        return self.title
    def is_expired(self):
        if date.today()>self.expiry_date:
            return True
        else:
            return False
            
