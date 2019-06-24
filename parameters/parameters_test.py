#
# parameters_test2.py
#


def make_parameters(*overlays, **overlay_categories):
    parameters = []

    for overlay_category, overlay in overlay_categories.items():

        parameters.extend([f'{overlay_category}: {overlay}'])

    return parameters


p = make_parameters(Email=('Count', 'Status'), Donation=('Amount'))

print(p)
