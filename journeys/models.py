from django.db import models

# Create your models here.

class Station(models.Model):
	id = models.AutoField(primary_key=True)
	station_name = models.CharField(max_length=128)
	station_code = models.CharField(max_length=128)
	station_lat  = models.FloatField(default=0.0)
	station_long = models.FloatField(default=0.0)
	
	def __unicode__(self):
		#return self.station_code
		return "%s, %s, %f, %f" % (self.station_name, self.station_code, self.station_lat, self.station_long)
	
class Train(models.Model):
	train_code = models.IntegerField(unique=True,primary_key=True)
	train_name = models.CharField(max_length=250)
	train_route = models.CharField(max_length=2000)

	def __unicode__(self):
		return "%s, %s, %s" % (self.train_code, self.train_name, self.train_route)
	
class Airport(models.Model):
	id = models.AutoField(primary_key=True)
	station_name = models.CharField(max_length=128)
	station_code = models.CharField(max_length=128)
	city_name = models.CharField(max_length=128)
	station_lat  = models.FloatField(default=0.0)
	station_long = models.FloatField(default=0.0)
	
	def __unicode__(self):
		#return self.station_code
		return "%s, %s, %s, %f, %f" % (self.station_name, self.station_code, self.city_name, self.station_lat, self.station_long)
	
class Plane(models.Model):
	plane_code = models.IntegerField(unique=True,primary_key=True)
	plane_name = models.CharField(max_length=250)
	plane_route = models.CharField(max_length=2000)

	def __unicode__(self):
		return "%s, %s, %s" % (self.plane_code, self.plane_name, self.plane_route)