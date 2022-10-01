from django.db import models
from django.utils import timezone
# Create your models here.

class Teams(models.Model) :
	teamname = models.CharField(max_length=250, primary_key=True)
	email = models.EmailField(max_length=250, unique=True)
	points = models.IntegerField(default=0)
	join = models.DateTimeField(auto_now_add=True, auto_now=False)
	latest = models.DateTimeField(default = timezone.now())