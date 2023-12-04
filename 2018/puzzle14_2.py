
target = "509671"
target_len = len(target)

scores = [3, 7]

elf1 = 0
elf2 = 1

i = 0
while True:

    new_scores = list([int(c) for c in str(scores[elf1] + scores[elf2])])

    for new_score in new_scores:
        scores.append(new_score)

        if str(new_score) == target[-1]:
            target_check = "".join([str(s) for s in scores[-target_len:]])

            if target_check == target:
                print(len(scores) - target_len)
                exit()

    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)
