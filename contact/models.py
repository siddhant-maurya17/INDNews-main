from django.db import models
from datetime import datetime
# Create your models here.
class Messages(models.Model):
  class Meta:
    verbose_name_plural = "Messages"
  name = models.CharField(max_length=20)
  email = models.EmailField(max_length=200)
  subject=models.CharField(max_length=100)
  message = models.TextField(max_length=600)
  date = models.DateTimeField(default=datetime.now())

  STATUS =[('Read','Read'), ('Unread','Unread'), ('Spam','Spam')]
  status = models.CharField(choices=STATUS,max_length=30,default='Unread')
  def __str__(self):
    return self.name