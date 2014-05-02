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

class Company(models.Model):

	company_name = models.CharField(max_length=100, required = True, unique=True)
	RFC = models.CharField(max_length=15, required = True, unique=True)
	identify = models.CharField(max_length=50)
	phone = models.ForeignKey(Phone)
	email = models.ForeignKey(Email)
	social_network = models.ForeignKey(SocialNetwork)
    web_page = models.URLField()
    company_type = models.OneToOneField(Company_type)

	class Meta:
		abstract = True

class Company_type(models.Model)
    company_type = models.CharFieldcompany_name = models.CharField(max_length=100, required = True, unique=True)