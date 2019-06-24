#
# search.py
#
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:

        if file.endswith('.py'):
            print(root+'/'+str(file))
