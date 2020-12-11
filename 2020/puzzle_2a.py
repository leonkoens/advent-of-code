import sys


with open('input_2.txt') as f:
    content = f.read()

content = [x.split(":") for x in content.strip().split("\n")]

valid = 0

for line in content:
    rules = line[0]
    password = line[1]

    length, letter = rules.split(" ")
    letter_min, letter_max = length.split("-")

    if int(letter_min) <= password.count(letter) <= int(letter_max):
        valid += 1

print(valid)
