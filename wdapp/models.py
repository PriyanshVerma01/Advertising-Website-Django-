from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    eno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return'message from' + self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    