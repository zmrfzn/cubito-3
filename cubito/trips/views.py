from django.shortcuts import render
from django.http import HttpResponse
from urllib2 import urlopen
from django.http import HttpRequest,HttpResponse
import json
from time import sleep

# Create your views here.
def index(request):
	trip_id = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php"))
	return HttpResponse(trip_id['trip_id'])
