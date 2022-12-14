from django.db import models
import hashlib

# Create your models here.

def get_upload_path(instance, filename) :
	return instance.category+'/challenges_{0}/{1}'.format(hashlib.md5(instance.name.encode('utf-8')).hexdigest(), filename)

class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True)
	##########################
	ordernum = models.IntegerField(default=1)
	challenge_id = models.CharField(max_length=300, primary_key=True)
	category = models.CharField(max_length=100)
	description = models.TextField()
	points = models.IntegerField()
	file = models.FileField(null=True, blank=True, upload_to=get_upload_path)
	flag = models.CharField(max_length=500)
	author = models.CharField(max_length=250)
	hint = models.TextField()
	hint_points = models.IntegerField(default=0)

class ChallengesSolvedBy(models.Model) :
	challenge_id =  models.CharField(max_length=250)
	user_name = models.CharField(max_length=250)
	points = models.IntegerField()