
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def erange(value):
	if value<10000000 or value>16000000:
		raise ValidationError("Invalid enrol Number")

class ProfileData(models.Model):	
	BRANCH_CHOICES=(('CSE','CSE'),('ECE','ECE'),('EE','EE'),('ME','ME'))
	user=models.OneToOneField(User)
	branch = models.CharField(max_length=200,choices=BRANCH_CHOICES)
	enrollment = models.IntegerField(default = 0     )
	gender = models.CharField(max_length=6,blank=False,choices=(('Male','Male'),('Female','Female')),default='Male')
	dob = models.DateField ( default = "1996-10-17"     )
	contact=models.BigIntegerField(default = 0 )
	address=models.CharField(max_length=200)
	about=models.CharField(max_length=300)
	profile=models.ImageField(upload_to='./profile/',default='/profile/default.jpg')
