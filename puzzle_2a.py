content = None

with open('input_2.txt', 'r') as handle:
    content = handle.readlines()

opcodes = [int(x) for x in content[0].split(',')]
opcodes[1] = 12
opcodes[2] = 2

limit = len(opcodes)
i = 0

while i < limit:

    if opcodes[i] == 99:
        break

    index = opcodes[i + 3]
    value = 0

    if opcodes[i] == 1:
        value = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]]

    elif opcodes[i] == 2:
        value = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]]

    opcodes[index] = value
    i += 4

print(opcodes[0])
