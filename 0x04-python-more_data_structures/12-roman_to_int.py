#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return(0)

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    var1 = 0

    for x in range(0, len(roman_string)):
        if x > 0 and roman[roman_string[x]] > roman[roman_string[x - 1]]:
            var1 += roman[roman_string[x]] - roman[roman_string[x - 1]] * 2
        else:
            var1 += roman[roman_string[x]]
    return (var1)
