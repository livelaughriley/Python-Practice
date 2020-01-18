#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Overlay:

    def __init__(self, name: str = "", num_fields: int = 0):
        self.name = name
        self.num_fields = num_fields

    def categorize(prefixes: list = [], fields: list = []):
        category = {}
        for prefix in prefixes:
            for field in fields:
                category[prefix] = field
                fields.remove(field)
        return category


dish = {
    "Education": ["Class Year", "Degree"],
    "Donor": ["Donor Status", "Lifetime Giving"]
}


# dish["Location"] = ["Country", "State"]
# print(dish)
