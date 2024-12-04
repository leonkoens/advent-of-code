import re


content = None
with open('3.txt', 'r') as handle:
    content = handle.read()

#content = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


total = 0
for result in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', content):
    a = int(result.group(1))
    b = int(result.group(2))

    total += a * b

print(total)
