import re
from collections import deque
from operator import mul
from functools import reduce


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()


#content = """
#Monkey 0:
#  Starting items: 79, 98
#  Operation: new = old * 19
#  Test: divisible by 23
#    If true: throw to monkey 2
#    If false: throw to monkey 3
#
#Monkey 1:
#  Starting items: 54, 65, 75, 74
#  Operation: new = old + 6
#  Test: divisible by 19
#    If true: throw to monkey 2
#    If false: throw to monkey 0
#
#Monkey 2:
#  Starting items: 79, 60, 97
#  Operation: new = old * old
#  Test: divisible by 13
#    If true: throw to monkey 1
#    If false: throw to monkey 3
#
#Monkey 3:
#  Starting items: 74
#  Operation: new = old + 3
#  Test: divisible by 17
#    If true: throw to monkey 0
#    If false: throw to monkey 1
#""".strip().split("\n")


class MonkeyList:
    monkeys = []
    divisor = 0


class Monkey:

    def __init__(self):
        self.items = deque()
        thrown = []
        self.operation = ()
        self.test = None
        self.true_case = None
        self.false_case = None
        self.items_inspected = 0

    def __repr__(self):
        return f'{self.items}'

    def inspect_items(self):

        for i in range(len(self.items)):
            self.items_inspected += 1
            item = self.items.popleft()
            variable = self.operation[1]

            if variable == 'old':
                variable = item
            else:
                variable = int(variable)

            if self.operation[0] == '+':
                item += variable

            elif self.operation[0] == '*':
                item *= variable

            #item //= 3

            item = item % MonkeyList.divisor
            
            if item % self.test == 0:
                MonkeyList.monkeys[self.true_case].items.append(item)
            else:
                MonkeyList.monkeys[self.false_case].items.append(item)

    

items_re = re.compile('\s+Starting items: (.+)')
operation_re = re.compile('\s+Operation: new = old (.+)')
test_re = re.compile('\s+Test: divisible by (\d+)')
true_re = re.compile('\sIf true: throw to monkey (\d)')
false_re = re.compile('\sIf false: throw to monkey (\d)')

monkey = None


for line in content:
    if line.startswith('Monkey'):
        monkey = Monkey()
        MonkeyList.monkeys.append(monkey)
        continue


    if match := items_re.search(line):
        monkey.items = deque([int(item) for item in match.group(1).split(', ')])

    elif match := operation_re.search(line):
        operator, number = match.group(1).split(' ')
        monkey.operation = operator, number

    elif match := test_re.search(line):
        monkey.test = int(match.group(1))

    elif match := true_re.search(line):
        monkey.true_case = int(match.group(1))

    elif match := false_re.search(line):
        monkey.false_case = int(match.group(1))


MonkeyList.divisor = reduce(mul, [monkey.test for monkey in MonkeyList.monkeys], 1)

number_of_monkeys = len(MonkeyList.monkeys)
for i in range(10000 * number_of_monkeys):
    MonkeyList.monkeys[i % number_of_monkeys].inspect_items()

inspected = [monkey.items_inspected for monkey in MonkeyList.monkeys]
a = max(inspected)
inspected.remove(a)
b = max(inspected)

print("Part 2", a*b, a, b, i)
    
