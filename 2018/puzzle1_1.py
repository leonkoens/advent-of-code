
content = ''
with open('input1.txt') as handle:
    content = handle.read()

content = content.replace("\n", "")
print(eval(content))

