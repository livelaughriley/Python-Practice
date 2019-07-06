#!/usr/bin/env python3
#
# making some loops :)
#

names = 'riley', 'mhyssa', 'mom', 'scoop'
nums = 1, 2, 3, 4, 5, 6


def make_list(strings: str, *stringsx):
    _list = []
    for string in strings:
        _list.append(string)
    return _list


def list_details(_list, *_lists):
    print('This is the list: %s \n' % _list)
    try:
        print(f"List: {_list} \n"
              f'Length: {len(_list)}. \n'
              f"Flattened: {', '.join(str(string) for string in _list)} \n"
              f"Type: {type(_list)} \n")
    except Exception:
        print("There was an error.")
        print(f'{type(_list)}')
        raise


def list_compare(_list_one: list, _list_two: list):
    for i in range(len(_list_one)):
        if i in range(len(_list_two)):
            print(f'{i} is in {_list_one}')
            print(f'{i} is at list two: [{_list_two[i]}]')
        else:
            print(f'{i} is not in {nums}')


names_list = make_list(names)

nums_list = make_list(nums)

print(f"""
      names_list: {names_list}
      nums_list : {nums_list}
      """)

list_compare(names_list, nums_list)
