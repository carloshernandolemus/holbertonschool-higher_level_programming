#!/usr/bin/python3
''' this functions get peak in a list '''


def find_peak(list_of_integers):
    ''' find a peak '''
    peak = 0
    list_ = list_of_integers
    for idx, i in enumerate(list_):
        if idx - 1 == -1:
            if idx + 1 == len(list_) or list_[idx+1] < i:
                peak = i
                break
            else:
                peak = i
                continue
        if (list_[idx-1] < i) and (idx + 1 == len(list_) or list_[idx+1] < i):
            peak = i
            break
    return peak
