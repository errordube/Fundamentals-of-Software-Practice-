#
#  IMPORTANT: DO NOT MAKE ANY CHANGES TO THIS FILE
#

# import module that defines unit-testing framework
import unittest

# import module project1.py containing functions to test
import project1

class Project1Test(unittest.TestCase):

    def test_monthly_car_payment_1(self):
        result = project1.monthly_car_payment(20000,6,12)
        self.assertEqual(round(result,2),1721.33)

    def test_monthly_car_payment_2(self):
        result = project1.monthly_car_payment(20000,6,24)
        self.assertEqual(round(result,2),886.41)

    def test_monthly_car_payment_3(self):
        result = project1.monthly_car_payment(20000,6,36)
        self.assertEqual(round(result,2),608.44)

    def test_monthly_car_payment_4(self):
        result = project1.monthly_car_payment(20000,6,48)
        self.assertEqual(round(result,2),469.70)

    def test_monthly_car_payment_5(self):
        result = project1.monthly_car_payment(20000,6,60)
        self.assertEqual(round(result,2),386.66)

    def test_n_factorial_1(self):
        result = project1.n_factorial(1)
        self.assertEqual(round(result,2),1.00)

    def test_n_factorial_2(self):
        result = project1.n_factorial(2)
        self.assertEqual(round(result,2),2.00)

    def test_n_factorial_3(self):
        result = project1.n_factorial(3)
        self.assertEqual(round(result,2),6.00)

    def test_n_factorial_4(self):
        result = project1.n_factorial(4)
        self.assertEqual(round(result,2),23.99)

    def test_n_factorial_5(self):
        result = project1.n_factorial(5)
        self.assertEqual(round(result,2),119.97)

    def test_easter_sunday_1(self):
        self.assertEqual(project1.easter_sunday(2001),'April 15')

    def test_easter_sunday_2(self):
        self.assertEqual(project1.easter_sunday(2005),'March 27')

    def test_easter_sunday_3(self):
        self.assertEqual(project1.easter_sunday(2010),'April 4')

    def test_easter_sunday_4(self):
        self.assertEqual(project1.easter_sunday(20015),'April 5')

    def test_easter_sunday_5(self):
        self.assertEqual(project1.easter_sunday(2020),'April 12')

    def test_income_tax_1(self):
        result = project1.income_tax(40000)
        self.assertEqual(round(result,2),400.00)

    def test_income_tax_2(self):
        result = project1.income_tax(60000)
        self.assertEqual(round(result,2),700.00)

    def test_income_tax_3(self):
        result = project1.income_tax(90000)
        self.assertEqual(round(result,2),1450.00)

    def test_income_tax_4(self):
        result = project1.income_tax(150000)
        self.assertEqual(round(result,2),3750.00)

    def test_income_tax_5(self):
        result = project1.income_tax(350000)
        self.assertEqual(round(result,2),12750.00)

    def test_income_tax_6(self):
        result = project1.income_tax(600000)
        self.assertEqual(round(result,2),26250.00)

    def test_bmi_category_1(self):
        self.assertEqual(project1.bmi_category(100,65),'Underweight')

    def test_bmi_category_2(self):
        self.assertEqual(project1.bmi_category(145,65),'Normal')

    def test_bmi_category_3(self):
        self.assertEqual(project1.bmi_category(160,65),'Overweight')

    def test_bmi_category_4(self):
        self.assertEqual(project1.bmi_category(200,65),'Obese')

    def test_bmi_category_5(self):
        self.assertEqual(project1.bmi_category(150,72),'Normal')

    def test_day_number_of_date_1(self):
        self.assertEqual(project1.day_number_of_date(1,1,2021),1)

    def test_day_number_of_date_2(self):
        self.assertEqual(project1.day_number_of_date(2,28,2021),59)

    def test_day_number_of_date_3(self):
        self.assertEqual(project1.day_number_of_date(6,15,2021),166)

    def test_day_number_of_date_4(self):
        self.assertEqual(project1.day_number_of_date(12,31,2021),365)

    def test_day_number_of_date_5(self):
        self.assertEqual(project1.day_number_of_date(12,31,2020),366)

    def test_decimal_to_binary_1(self):
        self.assertEqual(project1.decimal_to_binary(4),'100')

    def test_decimal_to_binary_2(self):
        self.assertEqual(project1.decimal_to_binary(10),'1010')

    def test_decimal_to_binary_3(self):
        self.assertEqual(project1.decimal_to_binary(100),'1100100')

    def test_decimal_to_binary_4(self):
        self.assertEqual(project1.decimal_to_binary(0),'0')

    def test_decimal_to_binary_5(self):
        self.assertEqual(project1.decimal_to_binary(15),'1111')

    def test_binary_to_decimal_1(self):
        self.assertEqual(project1.binary_to_decimal('100'),4)

    def test_binary_to_decimal_2(self):
        self.assertEqual(project1.binary_to_decimal('1010'),10)

    def test_binary_to_decimal_3(self):
        self.assertEqual(project1.binary_to_decimal('1100100'),100)

    def test_binary_to_decimal_4(self):
        self.assertEqual(project1.binary_to_decimal('11'),3)

    def test_binary_to_decimal_5(self):
        self.assertEqual(project1.binary_to_decimal('1'),1)

    def test_is_prime_1(self):
        result = project1.is_prime(1)
        self.assertTrue(type(result) is bool)
        self.assertFalse(result)

    def test_is_prime_2(self):
        result = project1.is_prime(3)
        self.assertTrue(type(result) is bool)
        self.assertTrue(result)

    def test_is_prime_3(self):
        result = project1.is_prime(10)
        self.assertTrue(type(result) is bool)
        self.assertFalse(result)

    def test_is_prime_4(self):
        result = project1.is_prime(17)
        self.assertTrue(type(result) is bool)
        self.assertTrue(result)

    def test_is_prime_5(self):
        result = project1.is_prime(23)
        self.assertTrue(type(result) is bool)
        self.assertTrue(result)

    def test_prime_numbers_1(self):
        self.assertEqual(project1.prime_numbers(20).strip(),"2 3 5 7 11 13 17 19")

    def test_prime_numbers_2(self):
        self.assertEqual(project1.prime_numbers(15).strip(),"2 3 5 7 11 13")

    def test_prime_numbers_3(self):
        self.assertEqual(project1.prime_numbers(25).strip(),"2 3 5 7 11 13 17 19 23")

    def test_prime_numbers_4(self):
        self.assertEqual(project1.prime_numbers(30).strip(),"2 3 5 7 11 13 17 19 23 29")


# run the unit tests in this script
if __name__ == '__main__':
    unittest.main(verbosity=2)
