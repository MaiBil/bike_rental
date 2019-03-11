import unittest
from rent.bike_rental import Rental


class RentalTest(unittest.TestCase):

    def test_one_bike_one_hour(self):
        app = Rental('hour', 1, 1)
        self.assertEqual(app.rent_bikes(), 5, 'Wrong price for rental of 1 bike 1 hour')

    def test_one_bike_three_hours(self):
        app = Rental('hour', 3, 1)
        self.assertEqual(app.rent_bikes(), 15, 'Wrong price for rental of 1 bike 3 hours')

    def test_two_bikes_two_hours(self):
        app = Rental('hour', 2, 2)
        self.assertEqual(app.rent_bikes(), 20, 'Wrong price for rental of 2 bikes 2 hours')

    def test_four_bikes_seven_hour(self):
        app = Rental('hour', 7, 4)
        self.assertEqual(app.rent_bikes(), 98, 'Wrong price for rental of 4 bikes 7 hours')

    def test_one_bike_one_day(self):
        app = Rental('day', 1, 1)
        self.assertEqual(app.rent_bikes(), 20, 'Wrong price for rental of 1 bike 1 day')

    def test_one_bike_three_days(self):
        app = Rental('day', 3, 1)
        self.assertEqual(app.rent_bikes(), 60, 'Wrong price for rental of 1 bike 3 days')

    def test_two_bikes_four_days(self):
        app = Rental('day', 4, 2)
        self.assertEqual(app.rent_bikes(), 160, 'Wrong price for rental of 2 bikes 4 days')

    def test_four_bikes_six_days(self):
        app = Rental('day', 6, 4)
        self.assertEqual(app.rent_bikes(), 336, 'Wrong price for rental of 4 bikes 6 days')

    def test_one_bike_one_week(self):
        app = Rental('week', 1, 1)
        self.assertEqual(app.rent_bikes(), 60, 'Wrong price for rental of 1 bike 1 week')

    def test_one_bike_three_weeks(self):
        app = Rental('week', 3, 1)
        self.assertEqual(app.rent_bikes(), 180, 'Wrong price for rental of 1 bike 3 weeks')

    def test_two_bikes_four_weeks(self):
        app = Rental('week', 4, 2)
        self.assertEqual(app.rent_bikes(), 480, 'Wrong price for rental of 2 bikes 4 weeks')

    def test_four_bikes_six_weeks(self):
        app = Rental('week', 6, 4)
        self.assertEqual(app.rent_bikes(), 1008, 'Wrong price for rental of 4 bikes 6 weeks')

    def test_invalid_bikes_amount_should_fail(self):
        app = Rental('hour', 1, 0)
        self.assertRaises(ValueError, app.rent_bikes)

    def test_invalid_units_amount_should_fail(self):
        app = Rental('hour', 0, 1)
        self.assertRaises(ValueError, app.rent_bikes)

    def test_invalid_type_should_fail(self):
        app = Rental('month', 1, 1)
        self.assertRaises(ValueError, app.rent_bikes)


if __name__ == '__main__':
    unittest.main()
