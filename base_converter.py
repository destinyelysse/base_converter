def convert_binary_to_decimal(binary_value):
    value_to_convert = str(binary_value)
    decimal_result = 0
    current_digit = 0
    while len(value_to_convert) > 0:
        binary_digit = value_to_convert[-1]
        value_to_convert = value_to_convert[:-1]   
        decimal_result += int(binary_digit) * (2**current_digit)
        current_digit += 1
    return str(decimal_result)

def convert_decimal_to_binary(decimal_value):
    value_to_convert = decimal_value
    binary_result = ''
    while value_to_convert >= 1:
        binary_result = str(value_to_convert % 2) + binary_result
        value_to_convert = int(value_to_convert / 2)
    return binary_result

def convert_base_to_decimal(value, base):
    if base >10:
        return 'Base must be less than 10'
    value_to_convert = str(value)
    decimal_result = 0
    current_digit = 0
    while len(value_to_convert) > 0:
        next_digit = value_to_convert[-1]
        value_to_convert = value_to_convert[:-1]   
        decimal_result += int(next_digit) * (base**current_digit)
        current_digit += 1
    return str(decimal_result)

def convert_decimal_to_base(value, base):
    if base >10:
        return 'Base must be less than 10'
    value_to_convert = int(value)
    converted_digit = ''
    while value_to_convert >= 1:
        next_digit = str(value_to_convert % base)
        converted_digit =  next_digit + converted_digit
        value_to_convert = int(value_to_convert / base)
    if base == 2:
        converted_digit = '0b'+converted_digit
    elif base == 8:
        converted_digit = '0o'+converted_digit
    return converted_digit

def convert_base_to_other_base(value, value_base, goal_base):
    decimal_value = convert_base_to_decimal(value, value_base)
    converted_value = convert_decimal_to_base(decimal_value, goal_base)
    return converted_value

print(str(convert_base_to_other_base(1977,10,8)))
