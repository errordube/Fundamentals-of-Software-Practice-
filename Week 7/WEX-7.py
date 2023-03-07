#
# Weekly Exercise #7: Classes in Python
# Author: Aditya Dube (G02500368)

import math

class Car(object):
    """Car class models a simple car."""

    def __init__(self, make, model, fuel_efficiency, fuel_in_tank = 0):
        """
        Initializes a car object with instance variables using parameter values.

        Parameters:
            make (str): make of car
            model (str): model of car
            fuel_efficiency (float): number of miles per gallon
            fuel_in_tank (float): amount of gas in the fuel tank

        Instance variables:
            _make: initialized with the value of parameter make
            _model: initialized with the value of parameter model
            _fuel_efficiency: initialized with the value of parameter fuel_efficiency
            _fuel_in_tank: initialized with the value of parameter fuel_in_tank

        Validations and Exceptions raised:
            ValueError if value of parameter fuel_efficiency is <= 0
            ValueError if value of parameter fuel_in_tank < 0
        """
        if fuel_efficiency <= 0:
            raise ValueError("Value for fuel efficiency must be a positive number.")
        if fuel_in_tank < 0:
            raise ValueError("Value for fuel in tank can't be a negative number.")
        self._make = make
        self._model = model
        self._fuel_efficiency = fuel_efficiency
        self._fuel_in_tank = fuel_in_tank

    def add_gas(self, amount_of_gas):
        """
        Adds gas to the car's fuel tank if the value of parameter amount_of_gas > 0.

        Parameters:
            amount_of_gas (float): amount of gas to add to car's tank
        """
        if amount_of_gas > 0:
            self._fuel_in_tank += amount_of_gas

    def gas_in_tank(self):
        """
        Returns the current amount of gas in the tank.
        """
        return self._fuel_in_tank

    def drive(self, miles):
        """
        Simulates driving car the specified number of miles.
        
        If miles is > 0 and there is enough gas in the tank, the amount of gas in the tank is reduced
        by the amount of gas required to drive the miles given.

        Parameters:
            miles (float): number of miles to drive
        """
        if miles > 0:
            gas_required = miles / self._fuel_efficiency
            if gas_required <= self._fuel_in_tank:
                self._fuel_in_tank -= gas_required
            else:
                self._fuel_in_tank = 0
    
    def __eq__(self, other):
        """
        Returns True if this (self) Car object is value equal to the other car object,
        False otherwise.

        Parameter:
            other: object to compare this object to
        """
        if not isinstance(other,Car):
            return False
        if self is other:
            return True
        return self._make == other._make and self._model == other._model and \
            math.isclose(self._fuel_efficiency,other._fuel_efficiency) and \
            math.isclose(self._fuel_in_tank,other._fuel_in_tank)

    def __str__(self):
        """
        Returns the string representation of self object.
        """
        return self.__repr__()

    def __repr__(self):
        """
        Returns the string representation of self object.
        """
        return f"Car({self._make},{self._model},{self._fuel_efficiency},{self._fuel_in_tank})"
        

#
# DO NOT MODIFY THE CODE IN THIS FUNCTION
#
def main():
    car1 = Car("Honda","Accord",20)
    print(car1)

    car2 = Car("Honda","Accord",20,0)
    print(car2)

    car3 = Car("Honda","Civic",20,10)
    print(car3)

    # checking if two variables have references to the same object
    print(car1 is car2)
    print(car1 is car3)
    print(car2 is car3)

    # checking if two variables have references to objects with same values for data attributes
    print(car1 == car2)
    print(car1 == car3)
    print(car2 == car3)
    print(car1 != car2)
    print(car2 != car3)

    car1.add_gas(15)
    car1.drive(100)
    print(car1)

    hybrid_car = Car("Toyota","Prius",50,10)
    print(hybrid_car)
    hybrid_car.drive(200)
    print(hybrid_car)
    
    try:
        lousy_car = Car("XYZ","Junk",0,10)
        print(lousy_car)
    except Exception as ex:
        print(ex)

    try:
        bad_car = Car("ABC","TBD",5,-5)
        print(bad_car)
    except Exception as ex:
        print(ex)


# call main() if this script is run as a top-level program
if __name__ == "__main__":
    main()

