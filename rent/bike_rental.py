class Rental:
    """
    This is a class for calculating the price of renting a bike.

    Attributes:
        time_unit (str): 'hour', 'day' or 'week'.
        amount_of_time (int): Number of hours, days or weeks.
        number_of_bikes (int): Number of bikes the user wants to rent.
    """

    prices = {'hour': 5, 'day': 20, 'week': 60}

    def __init__(self, time_unit, amount_of_time, number_of_bikes):
        """
        The constructor for Rental class.

        Parameters:
           time_unit (str): 'hour', 'day' or 'week'.
           amount_of_time (int): Number of hours, days or weeks.
           number_of_bikes (int): Number of bikes the user wants to rent.
        """

        self.time_unit = time_unit
        self.amount_of_time = amount_of_time
        self.number_of_bikes = number_of_bikes

    def rent_bikes(self):
        """
        The function to calculate the price for this rent.

        Returns:
            total_price (int): Total price of this rent.
        """

        if self.time_unit not in ['hour', 'day', 'week']:
            raise ValueError('Invalid time_unit value')

        if self.amount_of_time <= 0:
            raise ValueError('Invalid amount_of_time value')

        if self.number_of_bikes <= 0:
            raise ValueError('Invalid number_of_bikes value')

        if self.number_of_bikes >= 3 and self.number_of_bikes <= 5:
            discount = 0.7
        else:
            discount = 1

        total_price = self.prices[self.time_unit] * self.amount_of_time \
                      * self.number_of_bikes * discount

        return round(total_price)
