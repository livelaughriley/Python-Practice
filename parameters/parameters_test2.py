#
# parameters_test2.py
#


def make_parameters(*args, **kwargs):
    parameter = []

    for item in kwargs.items():
        overlay_category = item[0]
        overlay = item[1]

        parameter.extend([f'{overlay_category}: {overlay}'])

    print(parameter)


p = make_parameters(Email=('Count', 'Status'), Donation=('Amount'))
print(p)
