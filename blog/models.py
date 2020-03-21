from django.db import models

# create blog model
class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')


# add blog app to settings	
# BlogConfig in apps.py

# create migration
# python manage.py makemigrations

# migrate
# python manage.py migrate

# add to admin
# from .models import Blog

# admin.site.register(Blog)
