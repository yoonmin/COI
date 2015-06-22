from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage
import os

# If img with same name exists in media directory, replace it with new image
class OverwriteStorage(FileSystemStorage):
	def get_available_name(self, name):
		if self.exists(name):
			os.remove(os.path.join(settings.MEDIA_ROOT, name))
		return name


# Abstract base class for Faculty, Student, Visiting Scholar
class Person(models.Model):
	firstname 	= models.CharField(max_length=100)
	lastname 	= models.CharField(max_length=100)
	img 		= models.ImageField(upload_to='people', storage=OverwriteStorage())
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


class Faculty(Person):
	choices = (
		("D", "Director"),
		("A", "Associate Director"),
		("C", "Columbia Faculty Affiliate"),
		("E", "External Faculty Affiliate"),
	)
	category = models.CharField(max_length=1, choices=choices, default="D")


class Student(Person):
	choices = (
		("C", "Current Students"),
		("A", "Alumni"),
	)
	category = models.CharField(max_length=1, choices=choices, default="C")	


class VisitingScholar(Person):
	choices = (
		("C", "Current Visiting Scholar"),
		("P", "Past Visiting Scholar"),
	)
	category = models.CharField(max_length=1, choices=choices, default="C")


# Featured content (update needed)
class Featured(models.Model):
	category	= models.CharField(max_length=100, blank=True, null=True)
	name 		= models.CharField(max_length=100, blank=True, null=True)
	summary 	= models.TextField()
	cover		= models.ImageField(upload_to='featured', blank=True, storage=OverwriteStorage()) # Main cover image
	thumb 		= models.ImageField(upload_to='featured', blank=True, storage=OverwriteStorage()) # Thumbnail image

	title 		= models.CharField(max_length=200, blank=True, null=True)
	biography	= models.TextField(blank=True, null=True)
	cv			= models.URLField(blank=True, null=True)
	website		= models.URLField(blank=True, null=True)
	interest 	= models.TextField(blank=True, null=True)
	publication = models.TextField(blank=True, null=True)
	projects 	= models.TextField(blank=True, null=True)
	news		= models.TextField(blank=True, null=True)
	interview	= models.URLField(blank=True, null=True)
	
	order 		= models.IntegerField(default=0, blank=True, null=True)

	# Sulgify page name
	# (ex) "David Stark Interviewed on Bloomberg News"
	# -> Slugify: 	"david-stark-interviewed-on-bloomberg-news"
	# -> URL: 		http://www.columbia-coi.com/featured/david-stark-interviewed-on-bloomberg-news
	slug 		= models.SlugField(max_length=255, blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Featured, self).save(*args, **kwargs)	

	def __unicode__(self):
		return u'%s' % (self.title)



# http://www.columbia-coi.com/papers
class Paper(models.Model):
	title		= models.CharField(max_length=200, blank=True, null=True)
	author 		= models.CharField(max_length=200, blank=True, null=True)
	date 		= models.CharField(max_length=100, blank=True, null=True)
	abstract 	= models.TextField(blank=True, null=True)
	pdf			= models.FileField(upload_to='papers', blank=True, null=True, storage=OverwriteStorage())

	def __unicode__(self):
		return u'%s' % (self.title)













