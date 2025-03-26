def convert_decimal_to_binary(decimal_value):
    value_to_convert = decimal_value
    binary_result = ''
    while value_to_convert >= 1:
        binary_result = str(value_to_convert % 2) + binary_result
        value_to_convert = int(value_to_convert / 2)
    return binary_result

print(convert_decimal_to_binary(11))