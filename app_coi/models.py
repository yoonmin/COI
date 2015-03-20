from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

class People(models.Model):
	firstname 	= models.CharField(max_length=100)
	lastname 	= models.CharField(max_length=100)
	img 		= models.ImageField(upload_to='people')
	description = models.TextField()
	email 		= models.EmailField(blank=True)
	website 	= models.URLField(blank=True)

	def __unicode__(self):
		return u'%s' % (self.firstname + " " + self.lastname)

	def as_json(self):
		return {
			'firstname': self.firstname,
			'lastname': self.lastname,
			'img': self.img,
			'description': self.description,
			'email': self.email,
			'website': self.website,
		}

	class Meta:
		abstract = True	



class Faculty(People):
	choices = (
		("D", "Director"),
		("A", "Associate Director"),
		("C", "Columbia Faculty Affiliate"),
		("E", "External Faculty Affiliate"),
	)
	category = models.CharField(max_length=1, choices=choices, default="D")


class Student(People):
	choices = (
		("C", "Current Students"),
		("A", "Alumni"),
	)
	category = models.CharField(max_length=1, choices=choices, default="C")	



class VisitingScholar(People):
	choices = (
		("C", "Current Visiting Scholar"),
		("P", "Past Visiting Scholar"),
	)
	category = models.CharField(max_length=1, choices=choices, default="C")



class Featured(models.Model):
	category	= models.CharField(max_length=100, blank=True, null=True)
	name 		= models.CharField(max_length=100, blank=True, null=True)
	summary 	= models.TextField()
	cover		= models.ImageField(upload_to='featured', blank=True)
	thumb 		= models.ImageField(upload_to='featured', blank=True)

	title 		= models.CharField(max_length=200, blank=True, null=True)
	biography	= models.TextField(blank=True, null=True)
	cv			= models.URLField(blank=True, null=True)
	website		= models.URLField(blank=True, null=True)
	interest 	= models.TextField(blank=True, null=True)
	publication = models.TextField(blank=True, null=True)
	projects 	= models.TextField(blank=True, null=True)
	news		= models.TextField(blank=True, null=True)

	interview	= models.URLField(blank=True, null=True)
	
	slug 		= models.SlugField(max_length=255, blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Featured, self).save(*args, **kwargs)	

	def __unicode__(self):
		return u'%s' % (self.title)




class Paper(models.Model):
	title		= models.CharField(max_length=200, blank=True, null=True)
	author 		= models.CharField(max_length=200, blank=True, null=True)
	date 		= models.CharField(max_length=100, blank=True, null=True)
	abstract 	= models.TextField(blank=True, null=True)
	pdf			= models.FileField(upload_to='papers', blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.title)













