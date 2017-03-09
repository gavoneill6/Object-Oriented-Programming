import os, csv
import math
from Airport import Airport

class AirportAtlas:
	"""Atlas-like class that contains airport dictionary"""
	airport_fn = "airport.csv"

	def __init__(self, airport_file = airport_fn):
		self.airports = self.buildAirportDict(airport_file)

	def getAirport(self, airport_code):
		try:
			return self.airports[airport_code.upper()]
		except KeyError:
			return None	# displays None if airport code is invalid

	def buildAirportDict(self, filename):	# this builds a dictionary containing a specific airport's attributes
		airports = {}
		with open(os.path.join(filename), "rt", encoding="utf8") as f:
			reader = csv.reader(f)
			for row in reader:
				try:
					airports[row[4]] = Airport(row[4], row[1], row[3], row[2], float(row[6]), float(row[7]))
				except KeyError:
					continue # if country isn't found, the airport won't be added to dictionary
		return airports

	def distanceBetweenAirports(self, code1, code2): # I need to use my Distance.py file to work out this distance, how?

		distance = 0
		return distance

def main():

	if __name__ == "__main__":
		main()
