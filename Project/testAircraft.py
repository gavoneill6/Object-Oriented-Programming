from Aircraft import Aircraft # this runs without an error but doesn't give me the output I expected

jumbo = Aircraft("747")
print ("About to start preparing a ", jumbo.planeType, " for takeoff")
jumbo.addFuel(30)
jumbo.printStatus()
jumbo.fuelCheck()
jumbo.fly(500)

airbus = Aircraft("A330")
print ("About to start preparing a ", airbus.planeType, " for takeoff")
airbus.addFuel(2000)
airbus.printStatus()
airbus.fuelCheck()
airbus.fly(1000)

boeing = Aircraft("737")
print ("About to start preparing a ", boeing.planeType, " for takeoff")
fuelInTruck = 50000
fuelInTruck = boeing.addFuel(fuelInTruck)
boeing.printStatus()
boeing.fuelCheck()
boeing.fly(5000)
print("Fuel Truck still has: ", fuelInTruck)
