
target = 509671

scores = [3, 7]

elf1 = 0
elf2 = 1

i = 0
while len(scores) < target + 10:

    new_scores = list([int(c) for c in str(scores[elf1] + scores[elf2])])

    for new_score in new_scores:
        scores.append(new_score)

        if len(scores) == target+10:
            print("".join([str(s) for s in scores[-10:]]))
            exit()

    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)
