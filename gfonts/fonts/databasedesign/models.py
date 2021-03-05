from django.db import models
import datetime
import json
import requests
#import sqlite3

class font(models.Model):
	category = models.CharField(max_length = 20, default = "sans-serif")
	kind = models.CharField(max_length = 20, default = 'webfonts#webfont')
	family	= models.CharField("family", max_length = 25, default = "Arial")
	variants = models.CharField(max_length = 25, null = True)
	version = models.CharField(max_length = 20, default = "v12")
	lastModified = models.DateField()
	files = models.CharField(max_length = 300, null = True)
	#subsets = models.CharField(max_length = 25, null = True)


def json_response(API_KEY):
	response = requests.get("https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY).text
	py_response = json.loads(response)
	for i in py_response['items'][:2]:
		for variant in i['variants']:
			data =  font.objects.create(category = i['category'], family = i['family'], files = i['files'][variant],
										version = i['version'], kind = i['kind'], variants = variant,
										lastModified = i['lastModified']
										)
			data.save()

