from collections import Counter

content = '271973-785961'

input_range = content.split('-')

end = int(input_range[1])
numbers = list(input_range[0])
total = 0

while True:

    overwrite = -1

    for i in range(len(numbers)):

        if overwrite != -1:
            numbers[i] = overwrite
            continue

        try:
            if int(numbers[i+1]) < int(numbers[i]):
                overwrite = numbers[i]

        except IndexError:
            pass

    adjacent = 2 in Counter(numbers).values()
    check = int("".join(numbers))

    if check > end:
        break

    if adjacent:
        total += 1

    numbers = list(str(int("".join(numbers)) + 1))


print(total)
