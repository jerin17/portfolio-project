from django.db import models

# create blog model
class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')

	def summary(self):
		return self.body[:100] + ' . . . '

	def new_dt(self):
		return self.pub_date.strftime('%b %e %Y')

	def __str__(self):
		return self.title



# add blog app to settings	
# BlogConfig in apps.py

# create migration
# python manage.py makemigrations

# migrate
# python manage.py migrate

# add to admin
# from .models import Blog

# admin.site.register(Blog)
