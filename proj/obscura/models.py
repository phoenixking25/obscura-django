# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import os, uuid


# Create your models here.


class userSchema(models.Model):
	user = models.OneToOneField(User)
	college = models.CharField(max_length = 200)
	phone = models.IntegerField(help_text = "Enter user phone number", null = True )
	location = models.CharField(max_length = 200)
	currlevel = models.IntegerField(default = 1)

	def __str__(self):
		return self.user.username

class levelSchema(models.Model):
	user_profile = models.ForeignKey(userSchema,on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length = 100, help_text = "Enter the level name", null = True, blank = True)
	level_photo = models.ImageField(upload_to = 'level/', blank = True, null = True)
	ans = models.CharField(max_length = 200, help_text = "Enter the ans of the level")
	js = models.CharField(max_length = 500, help_text = "Enter the js if any available for this level",null = True, blank = True )

	def __str__(self):
		return self.name
