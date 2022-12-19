import json
import functools
import sys


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()


content = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip().split("\n")

a = None
b = None

pairs = []
pair = 0

def check_pair(a, b):
    a_len = len(a)
    b_len = len(b)

    for i in range(max(a_len, b_len)):
        try:
            a_value = a[i]
        except IndexError:
            return True
        try:
            b_value = b[i]
        except IndexError:
            return False

        if type(a_value) == int and type(b_value) == int:
            if a_value > b_value:
                return False
            if a_value < b_value:
                return True
            
            continue

        elif type(a_value) == list and type(b_value) == list:
            value = check_pair(a_value, b_value)

        elif type(a_value) == int:
            value = check_pair([a_value], b_value)

        elif type(b_value) == int:
            value = check_pair(a_value, [b_value])

        if value is True:
            return True

        if value is False:
            return False


    return None

packets = []

for line in content:
    line = line.strip()
    #print(line)

    if line == '':
        pair += 1

        if check_pair(a, b):
            pairs.append(pair)

        a = None
        b = None

        continue
    
    if a is None:
        a = json.loads(line)
        packets.append(a)

    elif b is None:
        b = json.loads(line)
        packets.append(b)
        

if check_pair(a, b):
    pairs.append(pair)

print(sum(pairs))

packets.append([[2]])
packets.append([[6]])

packets_sorted = sorted(packets, key=functools.cmp_to_key(check_pair))
for packet in packets_sorted:
    print(packet)
