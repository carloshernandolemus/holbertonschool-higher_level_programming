#!/usr/bin/python3
def search_replace(my_list, search, replace):
    var1 = [replace if x == search else x for x in my_list]
    return(var1)
