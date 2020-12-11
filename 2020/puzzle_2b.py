import sys


with open('input_2.txt') as f:
    content = f.read()

content = [x.split(":") for x in content.strip().split("\n")]

valid = 0

for line in content:
    rules = line[0]
    password = line[1].strip()

    length, letter = rules.split(" ")
    letter_min, letter_max = length.split("-")

    check = 0
    
    try:
        if password[int(letter_min)-1] == letter:
            check += 1
    except IndexError:
        pass

    try:
        if password[int(letter_max)-1] == letter:
            check += 1
    except IndexError:
        pass

    if check == 1:
        valid += 1

print(valid)
