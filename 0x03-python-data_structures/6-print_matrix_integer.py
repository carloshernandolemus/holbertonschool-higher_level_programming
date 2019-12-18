#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   for x in matrix:
      var1 = " "
      for y in x:
         print("{:d}".format(y), end='')
         if y != x[-1]:
            print(var1, end='')
      print()
