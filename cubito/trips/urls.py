from django.conf.urls import url 
from . import views as trips_view

urlpatterns = [
	url(r'^$',trips_view.index,name='index'),
	url(r'^$',trips_view.getTrip,name='GetTrip'),
]