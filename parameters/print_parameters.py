#
# parameters.py
#


class Overlays():

    def make_list(*args, **kwargs):
        for _overlay_category, _overlay in kwargs.items():

            yield(f'{_overlay_category}: {_overlay}')


o = Overlays.make_list(Email=('Category', 'Status'), Donation='Status')


for i in o:
    print(i)
