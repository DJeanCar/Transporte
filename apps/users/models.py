from django.db import models

class SocialNetwork(models.Model):
	types = (
			('Facebook', 'Facebook'),
			('Twitter', 'Twitter'),
			('Google Plus', 'Google Plus'),
			('Otro', 'Otro')
		)

	social = models.CharField(max_length=50)
	types = models.CharField(choices=types, max_length=50)


class Email(models.Model):
	types = (
			('Trabajo', 'Trabajo'),
			('Personal', 'Personal'),
			('Otro', 'Otro')
		)

	email = models.EmailField(max_length=100)
	types = models.CharField(choices=types, max_length=50)



class Phone(models.Model):

	types = (
			('Casa' , 'Casa'),
			('Movil', 'Movil'),
			('Nextel', 'Nextel'),
			('Trabajo', 'Trabajo'),
			('Otro', 'Otro') 
		)

	number = models.CharField(max_length=10)
	types = models.CharField(choices=types, max_length=50)

	def __unicode__(self):
		return '%s %s' % (self.number)

class Person(models.Model):

	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.ForeignKey(Phone)
	email = models.ForeignKey(Email)
	social_network = models.ForeignKey(SocialNetwork)
	  
	class Meta:
		abstract = True