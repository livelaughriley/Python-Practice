#
# parameters.py
#


class Overlays():

    def make_list(*args, **kwargs):
        parameters = []

        for item in kwargs.items():
            overlay_category = item[0]
            overlay = item[1]

            parameters.extend(f'{overlay_category}: {overlay}')
        yield(parameters)


o = Overlays.make_list(Email=('Category', 'Status'), Donation='Status')

for i in o:
    print(i)
