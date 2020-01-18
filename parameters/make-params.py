#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def group_overlays(groups: list = [], overlays: list = []):
    x = {}
    for group in groups:
        for overlay in overlays:
            x[group] = overlay
            overlays.remove(overlay)
    return x


a = 'Education'
b = ['Class Year', 'Degree']
c = "Donor"
d = ["Donor Status", "Lifetime Giving"]

z = ['Education', 'Donor']
zz = [['Class Year', 'Degree'], ['Donor Status', 'Lifetime Giving']]

e = group_overlays([a, c], [b, d])
parameters = group_overlays(z, zz)

for group in parameters:
    for overlay in parameters[group]:
        print(f"{group}: {overlay}")
