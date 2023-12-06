import string


content = ''
with open('input5.txt') as handle:
    content = list(handle.read().strip())


run = True

while run:

    i = 0
    delete = []

    while i < len(content):
        
        try:
            if content[i] in string.ascii_lowercase and content[i+1] == content[i].upper():
                delete.append(i)
                delete.append(i+1)
                i+=1

            elif content[i] in string.ascii_uppercase and content[i+1] == content[i].lower():
                delete.append(i)
                delete.append(i+1)
                i+=1

        except IndexError:
            pass
        
        i += 1

    run = False
    for i in reversed(delete):
        del content[i]
        run = True

print(len(content))
