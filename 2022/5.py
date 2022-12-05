import re
from collections import deque


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

PUZZLE_PART = 2

#content = """
#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#
#move 1 from 2 to 1
#move 3 from 1 to 3
#move 2 from 2 to 1
#move 1 from 1 to 2
#""".split("\n")

stacks = []

for line in content:

    if line.strip() == '':
        continue

    if not line.startswith('move') and not line.startswith(' 1   2   3'):
        i = 1

        while True:
            try:
                crate = line[i].strip()
            except IndexError:
                break

            if crate:
                index = int((i-1) / 4)

                while True:
                    try:
                        stacks[index].appendleft(crate)
                        break
                    except IndexError:
                        stacks.append(deque())

            i += 4

    if line.startswith('move'):
        match = re.match('move (\d+) from (\d+) to (\d+)', line)

        if match:
            number = int(match.group(1))
            stack_from = int(match.group(2)) -1
            stack_to = int(match.group(3)) -1

            sub = deque()
            for i in range(number):
                if PUZZLE_PART == 1:
                    stacks[stack_to].append(stacks[stack_from].pop())

                if PUZZLE_PART == 2:
                    sub.appendleft(stacks[stack_from].pop())

            if PUZZLE_PART == 2:
                stacks[stack_to].extend(sub)


print("Part", PUZZLE_PART, "".join([a[-1] for a in stacks]))
