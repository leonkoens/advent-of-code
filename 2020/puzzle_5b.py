import sys
import re


with open('input_5.txt') as f:
    content = f.read().strip().split("\n")

seats = []

for line in content:
    row = [0, 127]
    column = [0, 7]

    for char in line:
        
        if char == 'F':
            row[1] = int(row[1] - ((row[1] - row[0]) / 2))
        if char == 'B':
            row[0] = int(row[1] - ((row[1] - row[0]) / 2))

        if char == 'L':
            column[1] = int(column[1] - ((column[1] - column[0]) / 2))
        if char == 'R':
            column[0] = int(column[1] - ((column[1] - column[0]) / 2))

    seat_id = row[1] * 8 + column[1]
    seats.append(seat_id)
        
seats.sort()

for i in range(len(seats)):
    if seats[i+1] - seats[i] == 2:
        print(seats[i] + 1)
        break
