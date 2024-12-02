
content = None
with open('2.txt', 'r') as handle:
    content = handle.readlines()

#content = """7 6 4 2 1
#1 2 7 8 9
#9 7 6 2 1
#1 3 2 4 5
#8 6 4 4 1
#1 3 6 7 9""".splitlines()

safe_reports = 0

for report in content:
    levels = report.split()

    print(report)

    previous_level = None
    safe = True

    for i in range(len(levels)-1):
        level_diff = int(levels[i]) - int(levels[i+1])
        
        if abs(level_diff) > 3 or abs(level_diff) == 0:
            print("Too much difference detected")
            safe = False
            break

        if previous_level is None:
            previous_level = level_diff

        elif previous_level * level_diff < 0:
            print("Opposite sign detected")
            safe = False
            break
    
    if safe:
        safe_reports += 1
    
print(safe_reports)

            
