#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    var1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    var2 = roman_string
    romlist = [var1[i[0]] if var1[i[0]] >= var1[i[1]] else (-1*var1[i[0]])
             for i in zip(var2, var2[1:] + var2[-1])]
    var3 = sum(romlist)
    return (var3)
