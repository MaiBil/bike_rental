# Description
A company rents bikes under following options:
1. Rental by hour, charging $5 per hour
2. Rental by day, charging $20 a day
3. Rental by week, changing $60 a week
4. Family Rental, is a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price

# Assigment:
1. Implement a set of classes to model this domain and logic
2. Add automated tests to ensure a coverage over 85%
3. Use GitHub to store and version your code
4. Apply all the recommended practices you would use in a real project
5. Add a README.md file to the root of your repository to explain: your design, the development practices you applied and how run the tests.
Note: we don't expect any kind of application, just a set of classes with its automated tests.



# Design:
I divided my code into 2 files: app.py and rent/bike_rental.py
Inside rent/bike_rental.py I defined class Rental, where I calculate the total price of the rent and return it in the method rent_bikes.
In file app.py the user is asked to input the values for how many bikes they would like to rent and for how long.

There is also a third file, bike_rental_test, where the tests are written using unittest.

# Development practices:
I used pycodestyle to check against PEP8 style conventions

# How to run the tests:
Write on the command line, while on the path on the proyect ../intivefdv $ python3 bike_rental_test.py
