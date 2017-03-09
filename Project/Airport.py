class Airport:

	def __init__(self, airport_code, name, country_name, city, latitude, longitude): # here I've declared the attributes for the Airport class
		self._code = airport_code
		self._name = name
		self._country = country_name
		self._city = city
		self._latitude = float(latitude)
		self._longitude = float(longitude)

	def __str__(self):
		airportstr=""
		return "{} (Name: {}, {}, {}, lat:{}, lon:{})".format(self._code, self._name,
					self._city, self._country, self._latitude, self._longitude)
