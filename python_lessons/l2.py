#!/bin/python3

import datetime

from dateutil.parser import parse

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    #  parse string to datetime variable
    delta1 = parse(t1)
    # change timezone to UTC - to have common timezone
    delta1 = delta1.astimezone(datetime.timezone.utc)

    #  parse string to datetime variable
    delta2 = parse(t2)
    # change timezone to UTC - to have common timezone
    delta2 = delta2.astimezone(datetime.timezone.utc)

    # calculate delta and covert to seconds 
    delta = int(abs((delta1 - delta2).total_seconds()))
    
    return delta

if __name__ == '__main__':

    t = int(input())
    #t = 1 
    
    for t_itr in range(t):
        t1 = input()
        #t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = input()
        #t2 = "Sun 10 May 2015 13:54:36 -0000"
        delta = time_delta(t1, t2)

        print (delta)

