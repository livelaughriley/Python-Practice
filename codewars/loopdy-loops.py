#!/usr/bin/env python3
#
# making some loops :)
#

names = 'riley', 'mhyssa', 'mom', 'scoop'
nums = 1, 2, 3, 4, 5, 6


def make_list(args):
    _list = []
    for i in args:
        _list.append(i)
    return _list

# def print_list(list):
#     for i in range(len(list)):
#         print(list[i])


ml = make_list(names)
# for i in ml:
#    print(i)
print('This is the list: %s' % str(ml))
print(f'''
       The list, {ml}, has a length of {len(ml)}. \n\n
       This is {ml} flattened:
       {', '.join(ml)}
       ''')
