import copy
import math
import sys

content = None

with open('input_2.txt', 'r') as handle:
    content = handle.readlines()


class Computer:

    def __init__(self, opcodes: list):
        self.programm_opcodes = opcodes

    def run(self, noun: int, verb: int) -> int:

        opcodes = copy.copy(self.programm_opcodes)
        opcodes[1] = noun
        opcodes[2] = verb

        limit = len(opcodes)
        pointer = 0

        while pointer < limit:

            if opcodes[pointer] == 99:
                break

            index = opcodes[pointer + 3]
            value = 0

            if opcodes[pointer] == 1:
                value = opcodes[opcodes[pointer+1]] + opcodes[opcodes[pointer+2]]

            elif opcodes[pointer] == 2:
                value = opcodes[opcodes[pointer+1]] * opcodes[opcodes[pointer+2]]

            else:
                import pdb; pdb.set_trace()

            opcodes[index] = value
            pointer += 4

        return opcodes[0]


opcodes = [int(x) for x in content[0].split(',')]
computer = Computer(opcodes)

for i in range(1, 100):
    for j in range(1, 100):
        answer = computer.run(i, j)

        if answer == 19690720:
            print(100 * i + j)
            sys.exit()
