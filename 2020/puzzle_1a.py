import sys


with open('input_1.txt') as f:
    content = f.read()

content = [int(x) for x in content.strip().split("\n")]
limit = len(content)

for i in range(limit):
    for j in range(i+1, limit):
        if content[i] + content[j] == 2020:
            print(content[i] * content[j])
            sys.exit(0)
