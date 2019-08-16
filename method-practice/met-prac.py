#!/usr/bin/env python3


def add_two_to(self, a, b):
    x = self + a
    y = self + b
    return self, x, y


add_two_to(1, 4, 6)

myObj = 3

mySecObj = add_two_to(myObj, 3, 3)


def obj_info(*object):
    for i in object:
        print(f"{i}: {type(i)}")


obj_info(myObj)
