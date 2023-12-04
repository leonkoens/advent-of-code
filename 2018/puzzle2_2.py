import sys

content = ''
with open('input2.txt') as handle:
    content = handle.read().strip()


def check(a, b):
    
    difference = 0
    letters = []
    j = 0
    while j < 25:
        
        if a[j] != b[j]:
            difference += 1

            letters.append(j)

            if difference > 1:
                return False

        j+=1

    common = list(a)
    del common[letters[0]]
    common = "".join(common)
    print(common)
    return True


box_ids = list(set(content.split("\n")))
box_ids_len = len(box_ids)
i = 0
while i < box_ids_len:

    k = i+1
    while k < box_ids_len:
        if check(box_ids[i], box_ids[k]):
            sys.exit()

        k += 1
    i += 1
