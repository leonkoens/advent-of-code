import re


content = None
with open('3.txt', 'r') as handle:
    content = handle.read()

#content = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

total = 0
enabled = True

regexes = [
    '(mul)\((\d{1,3}),(\d{1,3})\)',
    "(don't)\(\)",
    "(do)\(\)",
]

regex = "|".join(regexes)

for result in re.finditer(regex, content):
    
    mul, a, b, dont, do = result.groups()

    if do:
        enabled = True

    if dont:
        enabled = False

    if mul and enabled:
        total += int(a) * int(b)

print(total)
