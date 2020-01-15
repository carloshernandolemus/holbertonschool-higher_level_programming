#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    var1 = []
    for var2 in range(list_length):
        try:
            var3 = my_list_1[var2] / my_list_2[var2]
        except ZeroDivisionError:
            print("division by 0")
            var3 = 0
        except TypeError:
            print("wrong type")
            var3 = 0
        except IndexError:
            print("out of range")
            var3 = 0
        finally:
            var1.append(var3)
    return(var1)
