def convert_decimal_to_binary(decimal_value):
    value_to_convert = decimal_value
    binary_result = ''
    while value_to_convert >= 1:
        binary_result = str(value_to_convert % 2) + binary_result
        value_to_convert = int(value_to_convert / 2)
    return binary_result

print(convert_decimal_to_binary(11))


def convert_binary_to_decimal(binary_value):
    value_to_convert = str(binary_value)
    decimal_result = 0
    current_digit = 0
    while len(value_to_convert) > 0:
        binary_digit = value_to_convert[-1]
        value_to_convert = value_to_convert[:-1]   
        decimal_result += int(binary_digit) * (2**current_digit)
        current_digit += 1
    return decimal_result

print(convert_binary_to_decimal(1011))