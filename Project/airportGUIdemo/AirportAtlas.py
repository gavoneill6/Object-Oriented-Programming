import os,csv
from Airport import Airport

class AirportAtlas:
    """ Atlas-like class that contains airport dictionary"""
    airport_fn = "csv/airport.csv"

    def __init__(self, airport_file = airport_fn):
        self.airports = self.buildAirportDict(airport_file)

    def getAirport(self, airport_code):
        try:
            return self.airports[airport_code.upper()]
        except KeyError:
            return None


    def getAirportPredictions(self, airport_code):
        airport_code=airport_code.upper()
        predict_list=[]
        for airport in list(self.airports.values()):
            if airport.code[0:len(airport_code)]==airport_code:
                predict_list.append(airport.name)
            if len(predict_list)>19:
                return predict_list

        return predict_list


    def buildAirportDict(self,filename):
        airports = {}
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                try:
                    airports[row[4]] = Airport(row[4], row[1], row[3],
                                               row[2], float(row[6]), float(row[7]))
                except KeyError:
                # If country isn't found, the airport won't be added to the dictionary
                    continue
        return airports

    def distanceBetweenAirports(self, code1, code2):
        #fill in code here
        distance = 1
        return distance

def main():

    atlas=AirportAtlas()
    print(atlas.getAirport('DUB'))
    print(atlas.distanceBetweenAirports('JFK','DUB'))

if __name__ == "__main__":
    main()