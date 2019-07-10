
def convert_roman_numeral_to_decimal(roman_numeral):

    roman_numeral_to_decimal_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                                     'C': 100, 'D': 500, 'M': 1000}

    decimal_return_value = 0

    if roman_numeral in roman_numeral_to_decimal_dict:

        decimal_return_value = roman_numeral_to_decimal_dict[roman_numeral]

    return decimal_return_value


def is_valid_roman_numeral(converted_roman_numeral):

    invalid_value = 0
    is_valid_numeral = True

    if converted_roman_numeral == invalid_value:

        is_valid_numeral = False

    return is_valid_numeral


def convert_roman_numeral_string_to_decimal(roman_numeral_string):

    converted_return_value = 0
    previous_converted_value = 0

    for roman_numeral in reversed(roman_numeral_string):

        converted_roman_numeral = convert_roman_numeral_to_decimal(roman_numeral)

        if is_valid_roman_numeral(converted_roman_numeral):

            if previous_converted_value > converted_roman_numeral:

                converted_return_value = converted_return_value - converted_roman_numeral

            else:

                converted_return_value = converted_return_value + converted_roman_numeral

            previous_converted_value = converted_roman_numeral

        else:

            raise TypeError('Invalid Roman Numeral')

    return converted_return_value


def main():

    convert_roman_numeral_string_to_decimal('III')

if __name__ == "__main__":
    main()
