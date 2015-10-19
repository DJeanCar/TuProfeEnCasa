from django.db import models

class Occupation(models.Model):

	occupation = models.CharField(max_length=50)

	def __unicode__(self):
		return self.occupation

# Create your models here.
class Teacher(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	dni = models.BigIntegerField()
	age = models.IntegerField()

	occupation = models.ForeignKey(Occupation)

	disponibilidad_horaria = models.TextField()
	trabajar_con_nosotros = models.TextField()
	cv = models.FileField(upload_to = 'teachers')

	contacted = models.BooleanField(default = False)

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)



