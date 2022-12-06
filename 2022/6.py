import re


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

#content = """
#mjqjpqmgbljsphdztnvjfqwrcgsmlb
#bvwbjplbgvbhsrlpgdmjqwftvncz
#nppdvjthqldpwncqszvftbrmjlhg
#nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
#zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
#""".strip().split("\n")


def search(limit, line):

    i = limit
    line_length = len(line)

    while i <= line_length:
        sub = set(line[i-limit:i])

        if len(sub) == limit:
            return i

        i += 1


for line in content:
    print("Part 1", search(4, line))
    print("Part 2", search(14, line))
