""" WRONG


list_of_printers = []
for i in [1, 2, 3]:
   def printer():
       print(i)
   list_of_printers.append(printer)
for func in list_of_printers:
   func()
"""


def printer():
    list_of_printers = []
    for i in [1, 2, 3]:
        print(i)
    list_of_printers.append(printer)


printer()
