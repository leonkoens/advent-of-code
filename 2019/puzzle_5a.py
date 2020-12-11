import copy

content = None

with open('input_5.txt', 'r') as handle:
    content = handle.readlines()


class Computer:

    def __init__(self, opcodes: list):
        self.programm_opcodes = opcodes

    def run(self, param: int) -> int:

        opcodes = copy.copy(self.programm_opcodes)

        limit = len(opcodes)
        pointer = 0

        while pointer < limit:

            if opcodes[pointer] == 99:
                break

            instruction = str(opcodes[pointer]).zfill(6)

            param_modes = [int(x) for x in list(instruction[:4])]
            instruction = int(instruction[4:])

            if instruction == 1:
                params = opcodes[pointer+1:pointer+4]
                opcodes = self.add(param_modes, params, opcodes)
                pointer += 4

            elif instruction == 2:
                params = opcodes[pointer+1:pointer+4]
                opcodes = self.multiply(param_modes, params, opcodes)
                pointer += 4

            elif instruction == 3:
                opcodes[opcodes[pointer + 1]] = param
                pointer += 2

            elif instruction == 4:
                print(">>", opcodes[opcodes[pointer + 1]])
                pointer += 2

        return opcodes[0]

    def add(self, param_modes, params, opcodes):

        if param_modes[-1] == 0:
            first = opcodes[params[0]]
        else:
            first = params[0]

        if param_modes[-2] == 0:
            second = opcodes[params[1]]
        else:
            second = params[1]

        opcodes[params[2]] = first + second

        return opcodes

    def multiply(self, param_modes, params, opcodes):

        if param_modes[-1] == 0:
            first = opcodes[params[0]]
        else:
            first = params[0]

        if param_modes[-2] == 0:
            second = opcodes[params[1]]
        else:
            second = params[1]

        opcodes[params[2]] = first * second

        return opcodes


opcodes = [int(x) for x in content[0].split(',')]
computer = Computer(opcodes)

computer.run(1)
