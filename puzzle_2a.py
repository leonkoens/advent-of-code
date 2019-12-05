import math


content = None

with open('input_2.txt', 'r') as handle:
    content = handle.readlines()

opcodes = [int(x) for x in content[0].split(',')]
opcodes[1] = 12
opcodes[2] = 2

#opcodes = [1, 0, 0, 0, 99]
#opcodes = [2, 3, 0, 3, 99]
#opcodes = [2, 4, 4, 5, 99, 0]
#opcodes = [1, 1, 1, 4, 99, 5, 6, 0, 99]

limit = len(opcodes)
i = 0

while i < limit:
    #print(opcodes[i])

    if opcodes[i] == 99:
        break

    index = opcodes[i + 3]
    value = 0

    if opcodes[i] == 1:
        value = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]

    elif opcodes[i] == 2:
        value = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

    else:
        import pdb; pdb.set_trace()

    opcodes[index] = value
    i += 4

print(opcodes[0])
