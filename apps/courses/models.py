from __future__ import unicode_literals
from django.db import models
from ..logreg.models import Users

# Create your models here.
class EnrollmentsManager(models.Manager):
	def register(self, **kwargs):
		errors = {}
		student = kwargs['student']
		classroom = kwargs['classroom']

		if not kwargs['student']:
			errors['student'] = 'Please select a User'
		elif not kwargs['classroom']:
			errors['classroom'] = 'Please select a Course'
		else:
			enrollment = self.create(id=classroom, user_id=student)
			return (True, self.filter())
		return (False, errors)

class Courses(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=300)
	user_id = models.ManyToManyField(Users)
	created_at = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)

	objects = EnrollmentsManager()





