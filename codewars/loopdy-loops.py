#!/usr/bin/env python3
#
# making some loops :)
#

names = 'riley', 'mhyssa', 'mom', 'scoop'
nums = 1, 2, 3, 4, 5, 6


def make_list(*args):
    _list = []
    for arg in args:
        _list.append(arg)
    return _list


def list_details(*args):
    print('This is the list: %s' % args)
    # try:
    #     print(f'''
    #           The list, {args}, has a length of {len(args)}. \n\n
    #           This is {args} flattened:
    #           {', '.join(args)}
    #           ''')
    # except Exception:
    #     print(f'{type(args)}')
    #     raise


def compare_objects():
    for i in range(len(ml)):
        if i in nums:
            print(f'{i} is in {nums}')
            print(f'{i} is at nums[{nums[i]}]')
        else:
            print(f'{i} is not in {nums}')


ml = make_list(names)
print(ml, *ml, sep='\n')
print(f'''
      ml  : {type(ml)}
      *ml : {type((*ml))}
      ()  : {type(('just', 'some', 'list'))}
      ''')
