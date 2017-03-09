import math		# this is imported to allow us to use the mathematical functions below

lat1 = 53.421333		# I need to figure out how to get these coordinates from the csv?
long1 = -6.270075
lat2 = 51.4775
long2 = -0.461389

def distance_on_unit_sphere(lat1, long1, lat2, long2):	# This will give us the greater circle distance between two airports

    # Convert latitude and longitude to spherical coordinates in radians.
	degrees_to_radians = math.pi/180.0

    # phi = 90 - latitude
	phi1 = (90.0 - lat1)*degrees_to_radians
	phi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
	theta1 = long1*degrees_to_radians
	theta2 = long2*degrees_to_radians

    # Compute spherical distance from spherical coordinates:
	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
	arc = math.acos( cos )*6371
	arc = int(arc)
	return arc

print(distance_on_unit_sphere(lat1,long1,lat2,long2))
