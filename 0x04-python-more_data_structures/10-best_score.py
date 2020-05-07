#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    my_list = sorted(a_dictionary.items(), key=lambda py: (py[1], py[0]))
    p, y = my_list[-1]
    return (p)
