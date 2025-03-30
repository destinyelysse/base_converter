digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_base_to_decimal(value, base):
    if base >35:
        return 'Base must be less than 35'
    value_to_convert = str(value)
    decimal_result = 0
    current_digit = 0
    while len(value_to_convert) > 0:
        next_digit = value_to_convert[-1]
        next_digit_value = digits.find(next_digit)
        print('next_digit_value: '+str(next_digit_value))
        value_to_convert = value_to_convert[:-1]   
        decimal_result += int(next_digit_value) * (base**current_digit)
        current_digit += 1
    return str(decimal_result)

def convert_decimal_to_base(value, base):
    if base >35:
        return 'Base must be less than 35'
    value_to_convert = int(value)
    converted_digit = ''
    while value_to_convert >= 1:
        next_amount_to_digitize = str(value_to_convert % base)
        next_digit = digits[int(next_amount_to_digitize)]
        print('next_digit: '+str(next_digit))
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

print(str(convert_base_to_other_base(30,10,16)))