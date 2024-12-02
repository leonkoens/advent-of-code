
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

def check_report(levels):

    previous_level = None

    for i in range(len(levels)-1):
        level_diff = int(levels[i]) - int(levels[i+1])
        
        if abs(level_diff) > 3 or abs(level_diff) == 0:
            #print("Too much difference detected")
            return False

        if previous_level is None:
            previous_level = level_diff

        elif previous_level * level_diff < 0:
            #print("Opposite sign detected")
            return False
        
    return True

for report in content:

    levels = report.split()

    if check_report(levels):
        safe_reports += 1
    else:
        for i in range(len(levels)):

            new_levels = levels[0:i] + levels[i+1:len(levels)]

            if check_report(new_levels):
                safe_reports += 1
                break
    
print(safe_reports)

            
