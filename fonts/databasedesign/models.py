from django.db import models
import datetime
import json
import requests

class font(models.Model):
	category = models.CharField(max_length = 20, default = "sans-serif")
	family	= models.CharField("family", max_length = 500, default = "Arial")
	version = models.CharField(max_length = 20, default = "v12")
	lastModified = models.DateField(default = datetime.date(2020,1,1))
	variants = models.ManyToManyField("variants")
	subsets = models.ManyToManyField("subsets")
	def __str__(self):
		return self.family

class subsets(models.Model):
	subsets = models.CharField(max_length = 25, blank = True)
	def __str__(self):
		return self.subsets

class variants(models.Model):
	variants = models.CharField(max_length = 25, blank = True)
	files = models.URLField(max_length = 300, null = True)
	def __str__(self):
		return self.variants

def add_to_database(API_KEY):
	json_response = requests.get("https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY).text
	response = json.loads(json_response)
	for item in response["items"]:
		obj = font.objects.create(lastModified = item["lastModified"], category = item["category"],
									family = item["family"], version = item["version"])
		for style in item["files"].items():
			variant = variants.objects.create(variants = style[0], files = style[1])
			obj.variants.add(variant)
		for s in item["subsets"]:
			subset = subsets.objects.create(subsets = s)
			obj.subsets.add(subset)