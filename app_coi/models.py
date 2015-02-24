from django.db import models

class People(models.Model):
	firstname 	= models.CharField(max_length=100)
	lastname 	= models.CharField(max_length=100)
	img 		= models.ImageField(upload_to='media/people')
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
		("AD", "Associate Director"),
		("CFA", "Columbia Faculty Affiliate"),
		("EFA", "External Faculty Affiliate"),
	)
	category = models.CharField(max_length=3, choices=choices, default="D")


class CurrentStudent(People):
	pass

class VisitingScholar(People):
	choices = (
		("C", "Current Visiting Scholar"),
		("P", "Past Visiting Scholar"),
	)
	category = models.CharField(max_length=1, choices=choices, default="C")


class Alumni(People):
	pass





