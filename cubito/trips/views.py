from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest,HttpResponse
from django.db import models
from trips.models import trips
from urllib2 import urlopen
import json
from time import sleep

# Create your views here.
def index(request):
	trip_id = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php"))
	db_obj = trips(trip_id=trip_id['trip_id'])
	db_obj.save()
	return HttpResponse(trip_id['trip_id'])
