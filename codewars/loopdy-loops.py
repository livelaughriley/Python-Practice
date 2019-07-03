#!/usr/bin/env python3
#
# making some loops :)
#

names = 'riley', 'mhyssa', 'mom', 'scoop'
nums = 1, 2, 3, 4, 5, 6


def make_list(strings):
    _list = []
    for string in strings:
        _list.append(string)
    return _list


def list_details(_list, *_lists):
    # print('This is the list: %s\n' % list)
    try:
        print(
            f"List: {_list} \n"
            f'Length: {len(_list)}. \n'
            f"Flattened: {', '.join(str(arg) for arg in _list)} \n"
            f"Type: {type(_list)} \n"
        )
    except Exception:
        print("There was an error.")
        print(f'{type(_list)}')
        raise


def compare_objects():
    for i in range(len(ml)):
        if i in nums:
            print(f'{i} is in {nums}')
            print(f'{i} is at nums[{nums[i]}]')
        else:
            print(f'{i} is not in {nums}')


ml = make_list(names)

# ld = list_details(ml)

list_details(ml)

# list_details(ml)
# list_details(*ml)

# print(ml, *ml, sep='\n')
# print(f'''
#       ml  : {type(ml)}
#       *ml : {type((*ml,))}
#       ()  : {type(('just', 'some', 'list'))}
#       ''')
