__author__ = 'hinesa'
class Airport(object):

    def __init__(self, airport_code, name, country_name, city, latitude, longitude):
        self.code = airport_code
        self.country = country_name
        self.city = city
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        airportstr=""
        return "{} (Name: {}, {},{} lat:{} lon:{})".format(
            self.code,self.name,self.city,self.country,self.latitude,self.longitude)


def main():

    myairport=Airport("DUB","Dublin","Dublin","Ireland","53.421333","-6.270075")
    print(myairport)


if __name__ == "__main__":
    main()