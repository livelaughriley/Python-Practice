#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Overlay:

    def __init__(self, prefix: str = "", fields: list = []):
        self.prefix = prefix
        self.fields = fields

    def add_field(self, field):
        self.fields.append(field)


donor = Overlay(prefix="Donor")
donor.fields = ["Donor Status"]
print(donor.prefix, donor.fields)

donor.add_field("Lifetime Giving")
print(donor.fields)

for i in donor.fields:
    print(f"{donor.prefix}: {i}")
