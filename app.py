from rent.bike_rental import Rental

if __name__ == '__main__':

    # Get type of rental (hour/day/week)
    while True:
        time_unit = input('What type of rental would you like? (Hour/Day/Week) ').lower()
        if time_unit in ['hour', 'day', 'week']:
            break
        else:
            print('Not a valid option! Try again')
            continue

    # Get amount of time (number of hours/days/weeks)
    while True:
        try:
            amount_of_time = int(input(f'For how many {time_unit}s would you like to rent? '))
            break
        except ValueError:
            print('Not a valid value! Try again')
            continue

    # Get number of bikes
    while True:
        try:
            number_of_bikes = int(input('And how many bikes would you like to rent? '))
            break
        except ValueError:
            print('Not a valid value! Try again')
            continue

    # Create an instance (this_rental) of class Rental with the values provided by the user
    this_rental = Rental(time_unit, amount_of_time, number_of_bikes)

    # Calculate the price for this rental
    total_price = this_rental.rent_bikes()

    # Renturn the total price of the rental to the user
    print(f'Total price: ${total_price}')
