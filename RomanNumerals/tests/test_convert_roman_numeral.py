import unittest
from main import (convert_roman_numeral_string_to_decimal,
                  convert_roman_numeral_to_decimal)


class RomanNumeralTestClass(unittest.TestCase):

    def test_convert_I_to_1(self):

        roman_numeral_test_string = 'I'
        expected_decimal_value = 1
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral I should equal 1.')

    def test_convert_V_to_5(self):

        roman_numeral_test_string = 'V'
        expected_decimal_value = 5
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral V should equal 5.')

    def test_convert_X_to_10(self):

        roman_numeral_test_string = 'X'
        expected_decimal_value = 10
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral X should equal 10.')

    def test_convert_L_to_50(self):

        roman_numeral_test_string = 'L'
        expected_decimal_value = 50
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral L should equal 50.')

    def test_convert_C_to_100(self):

        roman_numeral_test_string = 'C'
        expected_decimal_value = 100
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral C should equal 100.')

    def test_convert_D_to_500(self):

        roman_numeral_test_string = 'D'
        expected_decimal_value = 500
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral D should equal 500.')

    def test_convert_M_to_1000(self):

        roman_numeral_test_string = 'M'
        expected_decimal_value = 1000
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral M should equal 1000.')

    def test_convert_invalid_roman_numeral(self):

        roman_numeral_test_string = 'A'
        expected_decimal_value = 0
        decimal_value = convert_roman_numeral_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Invalid values should return 0')

    def test_convert_II_to_2(self):

        roman_numeral_test_string = 'II'
        expected_decimal_value = 2
        decimal_value = convert_roman_numeral_string_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral II should equal 2.')

    def test_convert_MMXII_to_2012(self):

        roman_numeral_test_string = 'MMXII'
        expected_decimal_value = 2012
        decimal_value = convert_roman_numeral_string_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral MMXII should equal 2012.')

    def test_convert_MDCCXXXII_to_1732(self):

        roman_numeral_test_string = 'II'
        expected_decimal_value = 2
        decimal_value = convert_roman_numeral_string_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral MDCCXXXII should equal 1732.')

    def test_convert_invalid_roman_numeral_string(self):

        roman_numeral_test_string = 'ABCD'
        with self.assertRaises(TypeError) as exception_context:
            decimal_value = convert_roman_numeral_string_to_decimal(roman_numeral_test_string)
        self.assertTrue('Invalid Roman Numeral' in str(exception_context.exception))

    def test_convert_IV_to_4(self):

        roman_numeral_test_string = 'IV'
        expected_decimal_value = 4
        decimal_value = convert_roman_numeral_string_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral IV should equal 4.')

    def test_convert_XLI_to_41(self):

        roman_numeral_test_string = 'XLI'
        expected_decimal_value = 41
        decimal_value = convert_roman_numeral_string_to_decimal(roman_numeral_test_string)
        self.assertEqual(expected_decimal_value, decimal_value, 'Roman Numeral XLI should equal 41.')