import copy
from dataclasses import dataclass
import re


content = None
#with open('5_test.txt', 'r') as handle:
with open('5.txt', 'r') as handle:
#with open('5_sjoerd.txt', 'r') as handle:
    content = handle.readlines()


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):

        seeds = []
        category_map = {
            'seed': {},
            'soil': {},
            'fertilizer': {},
            'water': {},
            'light': {},
            'temperature': {},
            'humidity': {},
        }
        source = None

        for line in self.content:
            if line.strip() == '':
                continue

            match = re.search('^seeds: (.+)', line)

            if match:
                tmp = list(map(int, match.group(1).split(' ')))
                for i in range(0, len(tmp), 2):
                    seeds.append((tmp[i], tmp[i]+tmp[i+1]))
                continue
            
            match = re.search('([a-z]+)-to-([a-z]+) map:', line)

            if match:
                source = match.group(1)
                continue
            
            drs, srs, r = map(int, line.split(' '))
            category_map[source][(srs, srs+r)] = srs, srs+r, drs, drs+r
                
        lowest = 9999999999999999999

        #seeds = sorted(seeds, key=lambda x: x[0])

        def resolve(start, end, categories):

            categories = copy.deepcopy(categories)

            try:
                category = categories.pop(0)
            except IndexError:
                return start

            for ss, se, ds, de in category_map[category].values():

                # Source completely in range
                if ss <= start < se and ss < end <= se:
                    # ss              se
                    # [....|-----|....]
                    new_start = start - ss + ds
                    new_end = end - ss + ds

                    return resolve(new_start, new_end, categories)

                # Source end in range
                if ss <= end <= se:
                    #         ss        se
                    # |-------[----|....]
                    new_end = end - ss + ds

                    return min(
                        # Part inside
                        resolve(ds, new_end, categories),
                        # Part outside
                        resolve(start, ss-1, [category] + categories),
                    )

                # Source start in range
                if ss <= start <= se:
                    # ss        se
                    # [....|----]----|
                    new_start = start - ss + ds

                    return min(
                        # Part inside
                        resolve(new_start, de, categories),
                        # Part outside
                        resolve(se+1, end, [category] + categories)
                    )
                
                # Range in source
                if ss > start and se < end:
                    #     ss      se
                    # |---[.......]----|

                    return min(
                        resolve(start, ss-1, [category] + categories),
                        resolve(ds, de, categories),
                        resolve(se+1, end, [category] + categories),
                    )
            
            return resolve(start, end, categories)

        for seed_range in seeds:
            start = seed_range[0]
            end = seed_range[1]

            range_lowest = resolve(start , end, list(category_map.keys()))
            lowest = min(range_lowest, lowest)
        
        print(lowest-1)


aoc = AdventOfCode(content)
aoc.run()
