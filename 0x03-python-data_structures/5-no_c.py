#!/usr/bin/python3
def no_c(my_string):
    var1 = [char for char in my_string if char not in 'Cc']
    var1 = ''.join(var1)
    return(var1)
