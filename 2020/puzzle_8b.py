import sys


with open('input_8.txt') as f:
    content = f.read().strip().split("\n")

acc = 0
index = 0
index_set = set()
flip_index = {}
flipped = False

try:
    while True:

        if index in index_set:
            acc = 0
            index = 0
            index_set = set()
            flipped = False
            continue

        index_set.add(index)

        cmd, num = content[index].split(" ")
        num = int(num)

        if not flipped and index not in flip_index:
            flip_index[index] = True
            flipped = True
            cmd = "jmp" if cmd == "nop" else "nop"

        if cmd == "acc":
            acc += int(num)
            index += 1
        if cmd == "jmp":
            index += num
        if cmd == "nop":
            index += 1

except IndexError:
    print(acc)

