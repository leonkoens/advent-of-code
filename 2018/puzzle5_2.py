import string


content = ''
with open('input5.txt') as handle:
    content = handle.read().strip()


shortest = 999999999

for letter in string.ascii_lowercase:

    polymer = content.replace(letter, '').replace(letter.upper(), '')
    polymer = list(polymer)

    run = True
    
    start = 0
    end = len(polymer)

    while run:

        delete = []
        first = True
        i = start
        new_end = 0

        while i < end:
            
            try:
                if (
                    (polymer[i] in string.ascii_lowercase and polymer[i+1] == polymer[i].upper())
                    or
                    (polymer[i] in string.ascii_uppercase and polymer[i+1] == polymer[i].lower())
                ):
                    delete.append(i)
                    delete.append(i+1)

                    if first:
                        start = max(0, i-1)
                        first = False

                    i+=1
                    new_end = i

            except IndexError:
                pass
            
            i += 1

        run = False
        for i in reversed(delete):
            del polymer[i]
            run = True

        end = new_end

    shortest = min(shortest, len(polymer))

print(shortest)
