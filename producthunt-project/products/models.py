from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
	title = models.CharField(max_length=100)
	url =  models.TextField(max_length=100)
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/', height_field=32, width_field=32)
	body = models.TextField(default=' ')
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y') 
