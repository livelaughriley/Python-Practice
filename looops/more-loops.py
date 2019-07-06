#!/usr/bin/env python3
# some more loops :)
#

names = ['loopsy', 'crab', 'pikachu', 'split', 'splat', 'splitsplat']
nums = range(3)

# for i in nums:
#     print(i)

# for i in names:
#     print(i)


def print_obs(*args):
    for i in args:
        print(i, type(i))


print_obs(nums, names)
