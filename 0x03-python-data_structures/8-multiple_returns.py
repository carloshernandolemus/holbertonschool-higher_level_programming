#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        var1 = None
    else:
        var1 = sentence[0]
    return(len(sentence), var1)
