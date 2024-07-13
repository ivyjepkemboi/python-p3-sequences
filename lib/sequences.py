#!/usr/bin/env python3

def print_fibonacci(length):
   
    if length == 0:
        print (list())

    elif length == 1:
        print ([0])

    elif length >= 2:
        new_list = [0, 1]

        while len(new_list) < length:
            new_var = new_list[-1] + new_list[-2]
            new_list.append(new_var)
            
        print (new_list)

    else:
        print ('out of range')
          

    