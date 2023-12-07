from dataclasses import dataclass
import re


content = None
with open('5_test.txt', 'r') as handle:
#with open('5.txt', 'r') as handle:
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
            #'location': {},
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
            category_map[source][(srs, srs+r)] = srs, drs, srs+r, drs+r
                
        lowest = 9999999999999999999

        seeds = sorted(seeds, key=lambda x: x[0])

        def resolve(start, end, categories):

            print(f'Resolving {start} {end} {categories}')
            print(f'>range {end-start}')

            old_start = start
            old_end = end

            try:
                category = categories.pop(0)
            except IndexError:
                print(start, end, categories)
                return start

            for cr in category_map[category].keys():

                source_start = cr[0]
                source_end = cr[1]

                ss, ds, se, de = category_map[category][cr]

                print(f'>checking {ss} - {se}')

                if source_start <= start < source_end:

                    new_start = start - ss + ds

                    if source_start < end <= source_end:
                        print(f'>fits completely in {ss} {se}')

                        new_end = end - ss + ds

                        print(f'>New start end {new_start} {new_end}')
                        print(f'>range {new_end-new_start}')

                        return resolve(new_start, new_end, categories)

                    else:
                        # End outside this range, resolve the 2 parts

                        print(f'>end outside {cr[0]} {cr[1]}')

                        r = se - start

                        return min(
                            # Part outside
                            resolve(se+1, end, [category] + categories),
                            # Part inside
                            resolve(new_start, de, categories)
                        )

                if ss < end <= se:

                    new_end = end - ss + ds

                    print(f'>end inside, start outside {cr[0]} {cr[1]}')

                    return min(
                        resolve(ds, new_end, categories),
                        resolve(start, ss-1, [category] + categories)
                    )
                
                if ss > start and se < end:
                    print(f'>range inside {cr[0]} {cr[1]}')

                    return min(
                        resolve(start, ss, [category] + categories),
                        resolve(ds, de, categories),
                        resolve(se, end, [category] + categories),
                    )
            
            return resolve(start, end, categories)
                
        for seed_range in seeds:
            start = seed_range[0]
            end = seed_range[1]

            range_lowest = resolve(start , end, list(category_map.keys()))
            lowest = min(range_lowest, lowest)
        
        print(lowest)


aoc = AdventOfCode(content)
aoc.run()
