#
#  IMPORTANT: DO NOT MAKE ANY CHANGES TO THIS FILE
#

# import module that defines unit-testing framework
import unittest

# import module project2.py containing functions to test
import project2

class Project2Test(unittest.TestCase):

    def test_digit_to_code_1(self):
        self.assertEqual(project2.digit_to_code(0),"||:::")

    def test_digit_to_code_2(self):
        self.assertEqual(project2.digit_to_code(1),":::||")

    def test_digit_to_code_3(self):
        self.assertEqual(project2.digit_to_code(2),"::|:|")

    def test_digit_to_code_4(self):
        self.assertEqual(project2.digit_to_code(3),"::||:")

    def test_digit_to_code_5(self):
        self.assertEqual(project2.digit_to_code(4),":|::|")

    def test_digit_to_code_6(self):
        self.assertEqual(project2.digit_to_code(5),":|:|:")

    def test_digit_to_code_7(self):
        self.assertEqual(project2.digit_to_code(6),":||::")

    def test_digit_to_code_8(self):
        self.assertEqual(project2.digit_to_code(7),"|:::|")

    def test_digit_to_code_9(self):
        self.assertEqual(project2.digit_to_code(8),"|::|:")

    def test_digit_to_code_10(self):
        self.assertEqual(project2.digit_to_code(9),"|:|::")

    def test_digit_to_code_11(self):
        self.assertRaises(ValueError,project2.digit_to_code,-1)

    def test_digit_to_code_12(self):
        self.assertRaises(ValueError,project2.digit_to_code,-5)

    def test_digit_to_code_13(self):
        self.assertRaises(ValueError,project2.digit_to_code,10)

    def test_digit_to_code_14(self):
        self.assertRaises(ValueError,project2.digit_to_code,15)

    def test_code_to_digit_1(self):
        self.assertEqual(project2.code_to_digit("||:::"),0)

    def test_code_to_digit_2(self):
        self.assertEqual(project2.code_to_digit(":::||"),1)

    def test_code_to_digit_3(self):
        self.assertEqual(project2.code_to_digit("::|:|"),2)

    def test_code_to_digit_4(self):
        self.assertEqual(project2.code_to_digit("::||:"),3)

    def test_code_to_digit_5(self):
        self.assertEqual(project2.code_to_digit(":|::|"),4)

    def test_code_to_digit_6(self):
        self.assertEqual(project2.code_to_digit(":|:|:"),5)

    def test_code_to_digit_7(self):
        self.assertEqual(project2.code_to_digit(":||::"),6)

    def test_code_to_digit_8(self):
        self.assertEqual(project2.code_to_digit("|:::|"),7)

    def test_code_to_digit_9(self):
        self.assertEqual(project2.code_to_digit("|::|:"),8)

    def test_code_to_digit_10(self):
        self.assertEqual(project2.code_to_digit("|:|::"),9)

    def test_code_to_digit_11(self):
        self.assertRaises(ValueError,project2.code_to_digit,":::::")

    def test_code_to_digit_12(self):
        self.assertRaises(ValueError,project2.code_to_digit,"|||||")

    def test_code_to_digit_13(self):
        self.assertRaises(ValueError,project2.code_to_digit,":|:|::|:")

    def test_code_to_digit_14(self):
        self.assertRaises(ValueError,project2.code_to_digit,"")

    def test_zipcode_to_barcode_1(self):
        self.assertEqual(project2.zipcode_to_barcode("95014"),"||:|:::|:|:||::::::||:|::|:::|||")

    def test_zipcode_to_barcode_2(self):
        self.assertEqual(project2.zipcode_to_barcode("49505"),"|:|::||:|:::|:|:||::::|:|:|:::||")

    def test_zipcode_to_barcode_3(self):
        self.assertEqual(project2.zipcode_to_barcode("49525"),"|:|::||:|:::|:|:::|:|:|:|::|:|:|")

    def test_zipcode_to_barcode_4(self):
        self.assertEqual(project2.zipcode_to_barcode("71270"),"||:::|:::||::|:||:::|||:::::||:|")

    def test_zipcode_to_barcode_5(self):
        self.assertEqual(project2.zipcode_to_barcode("98122"),"||:|::|::|::::||::|:|::|:||::|:|")

    def test_zipcode_to_barcode_6(self):
        self.assertEqual(project2.zipcode_to_barcode("98102"),"||:|::|::|::::||||:::::|:|||:::|")

    def test_zipcode_to_barcode_7(self):
        self.assertEqual(project2.zipcode_to_barcode("22202"),"|::|:|::|:|::|:|||:::::|:|::|:||")

    def test_zipcode_to_barcode_8(self):
        self.assertEqual(project2.zipcode_to_barcode("20148"),"|::|:|||::::::||:|::||::|::|:|:|")

    def test_zipcode_to_barcode_9(self):
        self.assertEqual(project2.zipcode_to_barcode("22182"),"|::|:|::|:|:::|||::|:::|:|:|:|:|")

    def test_zipcode_to_barcode_10(self):
        self.assertEqual(project2.zipcode_to_barcode("77479"),"||:::||:::|:|::||:::||:|:::||::|")

    def test_zipcode_to_barcode_11(self):
        self.assertEqual(project2.zipcode_to_barcode("48105"),"|:|::||::|::::||||::::|:|:::|:||")

    def test_zipcode_to_barcode_12(self):
        self.assertEqual(project2.zipcode_to_barcode("94583"),"||:|:::|::|:|:|:|::|:::||::::|||")

    def test_zipcode_to_barcode_13(self):
        self.assertRaises(ValueError,project2.zipcode_to_barcode,49505)

    def test_zipcode_to_barcode_14(self):
        self.assertRaises(ValueError,project2.zipcode_to_barcode,"495051234")

    def test_zipcode_to_barcode_15(self):
        self.assertRaises(ValueError,project2.zipcode_to_barcode,"49505-XYZ")

    def test_zipcode_to_barcode_16(self):
        self.assertRaises(ValueError,project2.zipcode_to_barcode,["49505-XYZ"])

    def test_barcode_to_zipcode_1(self):
        self.assertEqual(project2.barcode_to_zipcode("||:|:::|:|:||::::::||:|::|:::|||"),"95014")

    def test_barcode_to_zipcode_2(self):
        self.assertEqual(project2.barcode_to_zipcode("|:|::||:|:::|:|:||::::|:|:|:::||"),"49505")

    def test_barcode_to_zipcode_3(self):
        self.assertEqual(project2.barcode_to_zipcode("|:|::||:|:::|:|:::|:|:|:|::|:|:|"),"49525")

    def test_barcode_to_zipcode_4(self):
        self.assertEqual(project2.barcode_to_zipcode("||:::|:::||::|:||:::|||:::::||:|"),"71270")

    def test_barcode_to_zipcode_5(self):
        self.assertEqual(project2.barcode_to_zipcode("||:|::|::|::::||::|:|::|:||::|:|"),"98122")

    def test_barcode_to_zipcode_6(self):
        self.assertEqual(project2.barcode_to_zipcode("||:|::|::|::::||||:::::|:|||:::|"),"98102")

    def test_barcode_to_zipcode_7(self):
        self.assertEqual(project2.barcode_to_zipcode("|::|:|::|:|::|:|||:::::|:|::|:||"),"22202")

    def test_barcode_to_zipcode_8(self):
        self.assertEqual(project2.barcode_to_zipcode("|::|:|||::::::||:|::||::|::|:|:|"),"20148")

    def test_barcode_to_zipcode_9(self):
        self.assertEqual(project2.barcode_to_zipcode("|::|:|::|:|:::|||::|:::|:|:|:|:|"),"22182")

    def test_barcode_to_zipcode_10(self):
        self.assertEqual(project2.barcode_to_zipcode("||:::||:::|:|::||:::||:|:::||::|"),"77479")

    def test_barcode_to_zipcode_11(self):
        self.assertEqual(project2.barcode_to_zipcode("|:|::||::|::::||||::::|:|:::|:||"),"48105")

    def test_barcode_to_zipcode_12(self):
        self.assertEqual(project2.barcode_to_zipcode("||:|:::|::|:|:|:|::|:::||::::|||"),"94583")

    def test_barcode_to_zipcode_13(self):
        self.assertRaises(ValueError,project2.barcode_to_zipcode,49505)

    def test_barcode_to_zipcode_14(self):
        self.assertRaises(ValueError,project2.barcode_to_zipcode,"|||:|:::|::|:|:|:|::|:::||::::||||")

    def test_barcode_to_zipcode_15(self):
        self.assertRaises(ValueError,project2.barcode_to_zipcode,"||:|:::|::|:|:|:|::|:::||::::::|")

    def test_barcode_to_zipcode_16(self):
        self.assertRaises(ValueError,project2.barcode_to_zipcode,"|||||::|::|:|:|:|::|:::||::::::|")


# run the unit tests in this script
if __name__ == '__main__':
    unittest.main(verbosity=2)
