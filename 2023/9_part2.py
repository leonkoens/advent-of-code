
content = None
with open('9.txt', 'r') as handle:
    content = [line.strip() for line in handle.readlines()]


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):

        total = 0

        for line in self.content:
            data = [int(c) for c in line.split(' ')]


            all_diffs = [data]
            done = False

            while not done:
                diffs = []
                all_zero = True

                for i in range(len(data)):
                    try:
                        diff = data[i+1] - data[i]
                        all_zero &= diff == 0
                        diffs.append(diff)
                    except IndexError:
                        continue
                
                all_diffs.append(diffs)

                if all_zero:
                    done = True

                    for i in range(len(all_diffs)-2, -1, -1):
                        new = all_diffs[i][0] - all_diffs[i+1][0]
                        all_diffs[i].insert(0, new)

                    total += all_diffs[0][0]
                
                else:
                    data = diffs
        
        print(total)


aoc = AdventOfCode(content)
aoc.run()