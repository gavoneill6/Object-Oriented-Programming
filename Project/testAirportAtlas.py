from AirportAtlas import AirportAtlas

atlas = AirportAtlas()

print(atlas.getAirport('DUB'))  # this should work
print(atlas.getAirport('JFK'))  # this should also work
print(atlas.getAirport('111'))  #this should return the error exception
