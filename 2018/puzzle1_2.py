import sys

content = ''
with open('input1.txt') as handle:
    content = handle.read().strip()

current = 0
freqs = set()
freqs.add(current)

while True:

    for change in content.split("\n"):
        
        change = int(change)
        current += change

        if current in freqs:
            print(current)
            sys.exit()

        freqs.add(current)
