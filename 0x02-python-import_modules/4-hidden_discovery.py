#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    a = dir(hidden_4)
    for i in a:
        if i[:2] != "__":
            print("{:s}".format(i))
