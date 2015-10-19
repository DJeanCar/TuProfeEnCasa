from django.db import models

# Create your models here.
class Client(models.Model):

	full_name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=50)
	message = models.TextField()
	contacted = models.BooleanField(default = False)

	def __unicode__(self):
		return self.full_name