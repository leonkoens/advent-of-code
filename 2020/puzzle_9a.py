import sys


with open('input_9.txt') as f:
    content = f.read().strip().split("\n")

preamble = 25
numbers = []
i = 0

def check_for_sum(numbers, number):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) == number:
                #print(numbers[i], numbers[j], number)
                return True

    return False


for line in content:
    number = int(line)

    if i >= preamble and not check_for_sum(numbers[-preamble:], number):
        print(number)
        sys.exit()

    numbers.append(number)
    i += 1
