from django.db import models

# Create your models here.
class UserActivityPeriod(models.Model):
	real_name = models.CharField(max_length = 200)
	tz = models.CharField(max_length = 200)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return '{}'.format(self.real_name)