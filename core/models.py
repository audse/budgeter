from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Total(models.Model):
	amount = models.FloatField(default=0.00)

	def __str__(self):
		return "$" + str(self.amount)

class Entry(models.Model):
	amount = models.FloatField(default=0.00)
	date = models.DateTimeField(default=timezone.now)
	category = models.CharField(max_length=140, default="income")
	notes = models.CharField(max_length=140)
	positive = models.BooleanField(default=True)

	def __str__(self):
		if self.positive:
			sign = "+"
		else:
			sign = "-"
		return "Entry: " + sign + "$" + str(self.amount) + " from " + self.category

class Category(models.Model):
	name = models.CharField(max_length=140)

	def __str__(self):
		return self.name

