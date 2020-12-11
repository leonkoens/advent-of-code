import sys
import re


with open('input_4.txt') as f:
    content = f.read().strip()


class Passport:
    def __init__(self):
        self.fields = {}

    def is_valid_simple(self):
        if len(self.fields) == 8:
            return True

        if len(self.fields) == 7 and 'cid' not in self.fields:
            return True

        return False

    def is_valid(self):
        return self.is_valid_simple() and self.check_fields()

    def check_fields(self):
        
        if int(self.fields['byr']) < 1920 or int(self.fields['byr']) > 2002:
            #print('byr', self.fields['byr'])
            return False

        if int(self.fields['iyr']) < 2010 or int(self.fields['iyr']) > 2020:
            #print('iyr', self.fields['iyr'])
            return False

        if int(self.fields['eyr']) < 2020 or int(self.fields['eyr']) > 2030:
            #print('eyr', self.fields['eyr'])
            return False

        if not re.match(r'^#[0-9a-f]{6}$', self.fields['hcl']):
            #print('ecl', self.fields['hcl'])
            return False

        if not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', self.fields['ecl']):
            #print('ecl', self.fields['ecl'])
            return False

        if not re.match(r'^\d{9}$', self.fields['pid']):
            #print('pid', self.fields['pid'])
            return False

        m = re.match(r'^(\d+)(cm|in)$', self.fields['hgt'])
        if not m:
            #print('hgt', self.fields['hgt'])
            return False

        number = m.group(1)
        unit = m.group(2)

        if unit == 'cm':
            if int(number) < 150 or int(number) > 193:
                #print('hgt', self.fields['hgt'])
                return False
                
        if unit == 'in':
            if int(number) < 59 or int(number) > 76:
                #print('hgt', self.fields['hgt'])
                return False

        return True


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
