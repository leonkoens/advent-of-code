import sys


with open('input_8.txt') as f:
    content = f.read().strip().split("\n")

acc = 0
index = 0
index_set = set()

while True:

    if index in index_set:
        print(acc)
        sys.exit()

    index_set.add(index)

    cmd, num = content[index].split(" ")
    num = int(num)

    #print(cmd, num)

    if cmd == "acc":
        acc += int(num)
        index += 1
    if cmd == "jmp":
        index += num
    if cmd == "nop":
        index += 1

