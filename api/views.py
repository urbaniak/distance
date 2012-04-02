from django.http import HttpResponse
from urllib2 import urlopen
from urllib import urlencode
import math
import json


# from http://www.johndcook.com/python_longitude_latitude.html
def distance_on_unit_sphere(lat1, long1, lat2, long2):
	# Convert latitude and longitude to
	# spherical coordinates in radians.
	degrees_to_radians = math.pi / 180.0

	# phi = 90 - latitude
	phi1 = (90.0 - lat1) * degrees_to_radians
	phi2 = (90.0 - lat2) * degrees_to_radians

	# theta = longitude
	theta1 = long1 * degrees_to_radians
	theta2 = long2 * degrees_to_radians

	# Compute spherical distance from spherical coordinates.

	# For two locations in spherical coordinates
	# (1, theta, phi) and (1, theta, phi)
	# cosine( arc length ) =
	#	 sin phi sin phi' cos(theta-theta') + cos phi cos phi'
	# distance = rho * arc length

	cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
		math.cos(phi1) * math.cos(phi2))
	arc = math.acos(cos)

	# Remember to multiply arc by the radius of the earth
	# in your favorite set of units to get length.
	return arc


def calculate_distance(request):
	try:
		lat = float(request.GET.get('lat'))
		lng = float(request.GET.get('lng'))
	except:
		lat = False
		lng = False

	if lat is not False and lng is not False:
		params = {'address': 'White Bear Yard,144a Clerkenwell Road, EC1R 5DF, London', 'sensor': 'false'}
		url = 'https://maps.googleapis.com/maps/api/geocode/json?%s' % urlencode(params)

		data = json.loads(urlopen(url).read())

		distance = distance_on_unit_sphere(
			float(request.GET.get('lat')),
			float(request.GET.get('lng')),
			data['results'][0]['geometry']['location']['lat'],
			data['results'][0]['geometry']['location']['lng']
			)

		response = {
			'mile': distance * 3960,
			'km': distance * 6373,
		}

	else:
		response = {'error': 'Missing lat and/or lng parameter.'}

	return HttpResponse(json.dumps(response), mimetype='application/json')
