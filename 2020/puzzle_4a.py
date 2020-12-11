import sys


with open('input_4.txt') as f:
    content = f.read().strip()


class Passport:
    def __init__(self):
        self.fields = {}

    def is_valid(self):

        if len(self.fields) == 8:
            return True

        if len(self.fields) == 7 and 'cid' not in self.fields:
            return True

        return False

passport = Passport()
valid = 0

for line in content.split("\n"):
    
    if line == '':
        if passport.is_valid():
            valid += 1
        passport = Passport()
        continue

    for key,value in [x.split(':') for x in line.split(' ')]:
        passport.fields[key] = value

if passport.is_valid():
    valid += 1

print(valid)
