import time
import sys

target = 'Hello world'
guess = ''

for i, c in enumerate(target):
    j = ord(' ')
    while True:
        sys.stdout.write(f'\r{guess}{chr(j)}')
        sys.stdout.flush()
        time.sleep(0.01)
        if chr(j) == c:
            guess += c
            break
        j += 1

print('\n\nACCESS GRANTED')
