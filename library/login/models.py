from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=200)
	author_name = models.CharField(max_length=20)
	description = models.TextField()
    
