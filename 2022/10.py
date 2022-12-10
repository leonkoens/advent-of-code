import re


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    commands = (line.strip() for line in handle.readlines())


#content = None
#with open('10_test.txt', 'r') as handle:
#    commands = (line.strip() for line in handle.readlines())


inspect = 20
signal_strengths = []

register = 1
cycle = 0
current_command = None
current_command_cycles = 0


while True:

    cycle += 1

    if current_command is None:
        try:
            new_command = next(commands)
        except StopIteration:
            break

        current_command = new_command

        if new_command.startswith('noop'):
            current_command_cycles = 0

        if new_command.startswith('addx'):
            current_command_cycles = 2

    current_command_cycles -= 1

    if cycle == inspect:
        inspect += 40
        print(cycle, register)
        signal_strengths.append(cycle * register)

    
    if current_command_cycles <= 0:

        command = current_command
        current_command = None

        
        if command == 'noop':
            continue

        command, variable = command.split(' ')

        if command == 'addx':
            register += int(variable)


print(signal_strengths)
print("Part 1", sum(signal_strengths))
