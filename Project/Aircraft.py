class Aircraft:

	def __init__(self, planeType = "747", units = "imperial", manufacturer = "Boeing", range = "9800"):	# initialising Aircraft with attributes I want it to have
		self.planeType = planeType
		self._fuel = 0
		self._maxFuel = 0
		self._fuelCheck = False
		self._minFuel = 1000
		self._range = 0

	def fuelCheck(self):	# this will check if fuel is above minimum level and return true or false
		if self._fuel < self._minFuel:
			print("Fuel Check Failed: Current fuel below safe limit: ", self._fuel, "less than ", self._minFuel)
			self._fuelCheck = False
		else:
			print("Fuel Check Complete: ", self._fuel)
			self._fuelCheck = True

	def printStatus(self):	# this will just print fuel level when called
		print("Current Fuel: ", self._fuel)

	def addFuel(self, volume):	# this will addFuel when called and return how much we didn't use
		unusedFuel = 0

		if self._fuel + volume <= self._maxFuel:
			self._fuel = self._fuel + volume
		elif self._fuel + volume > self._maxFuel:
			self._fuel = self._maxFuel
			unusedFuel = volume - self._fuel
		return unusedFuel

	def fly(self, distance):	# this will fly the aircraft when the distance isn't out of range
		if distance <= self._range:
			self._range -= distance
		else:
			print("distance too far")
			return self._range
