import copy
import sys

content = None

with open('input_5.txt', 'r') as handle:
    content = handle.readlines()

#content = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'


def log(msg):
    print(msg)


class Computer:

    def __init__(self, opcodes: list):
        self.opcodes = opcodes
        self.pointer = 0

    def run(self, argument: int) -> int:

        limit = len(self.opcodes)
        self.pointer = 0

        while self.pointer < limit:

            if self.opcodes[self.pointer] == 99:
                break

            instruction = str(self.opcodes[self.pointer]).zfill(6)
            print(instruction)

            param_modes = [int(x) for x in list(instruction[:4])]
            instruction = int(instruction[4:])

            if instruction == 1:
                self.add(param_modes)

            elif instruction == 2:
                self.multiply(param_modes)

            elif instruction == 3:
                self.opcodes[self.opcodes[self.pointer + 1]] = argument
                self.pointer += 2

            elif instruction == 4:
                self.print(param_modes)

            elif instruction == 5:
                self.jump_if_true(param_modes)

            elif instruction == 6:
                self.jump_if_false(param_modes)

            elif instruction == 7:
                self.less_than(param_modes)

            elif instruction == 8:
                self.equals(param_modes)

            else:
                import pdb; pdb.set_trace()

        return self.opcodes[0]

    def get_values(self, param_modes: list, params: list) -> list:

        values = []

        for i in range(len(params)):

            if param_modes[-1 - i] == 0:
                values.append(self.opcodes[params[i]])
            else:
                values.append(params[i])

        return values

    def add(self, param_modes: list):
        log('add')
        params = self.opcodes[self.pointer + 1:self.pointer + 4]
        values = self.get_values(param_modes, params)

        self.opcodes[params[2]] = values[0] + values[1]
        self.pointer += 4

    def multiply(self, param_modes: list):
        log('multiply')
        params = self.opcodes[self.pointer + 1:self.pointer + 4]
        values = self.get_values(param_modes, params)

        self.opcodes[params[2]] = values[0] * values[1]
        self.pointer += 4

    def print(self, param_modes: list):
        log('print')
        params = self.opcodes[self.pointer + 1:self.pointer + 2]
        values = self.get_values(param_modes, params)
        print(">>", values[0])
        self.pointer += 2

    def jump_if_true(self, param_modes: list):
        log('jump-if-true')
        params = self.opcodes[self.pointer + 1:self.pointer + 3]
        values = self.get_values(param_modes, params)

        if values[0] != 0:
            self.pointer = values[1]
        else:
            self.pointer += 3

    def jump_if_false(self, param_modes: list):
        log('jump-if-false')
        params = self.opcodes[self.pointer + 1:self.pointer + 3]
        values = self.get_values(param_modes, params)

        if values[0] == 0:
            self.pointer = values[1]
        else:
            self.pointer += 3

    def less_than(self, param_modes: list):
        log('less-than')
        params = self.opcodes[self.pointer + 1:self.pointer + 4]
        values = self.get_values(param_modes, params)

        if values[0] < values[1]:
            self.opcodes[params[2]] = 1
        else:
            self.opcodes[params[2]] = 0

        self.pointer += 4

    def equals(self, param_modes: list):
        log('equals')
        params = self.opcodes[self.pointer + 1:self.pointer + 4]
        values = self.get_values(param_modes, params)

        if values[0] == values[1]:
            self.opcodes[params[2]] = 1
        else:
            self.opcodes[params[2]] = 0

        self.pointer += 4


opcodes = [int(x) for x in content[0].split(',')]
#opcodes = [int(x) for x in content.split(',')]

computer = Computer(opcodes)
computer.run(5)

#for i in range(10):
#    computer.run(i)

