import unittest
from AirportAtlas import AirportAtlas 


class AtlasDistanceTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.known_values = (("DUB", "SYD", 17215), ("DUB", "AAL", 1096), ("DUB","CDG", 784))
        self.testAtlas = AirportAtlas("airport.csv")

        
    def test_getDistBetween_known_values(self):
        for code_1, code_2, dist in self.known_values:
            
            result = self.testAtlas.get_dist_between_airports(code_1, code_2)

            self.assertEqual(dist, result)

    def test_distance_between_dublin_is_zero(self):
        code_1 = 'DUB'
        code_2 = 'DUB'
        dist = 0
        result = self.testAtlas.get_dist_between_airports(code_1, code_2)
        self.assertEqual(dist, result)
        

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
