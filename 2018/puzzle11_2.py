import sys

serial_number = 7672
grid_size = 300


def power_level(x, y, serial_number):
    
    rack_id = x + 10
    power_level = ((rack_id * y) + serial_number) * rack_id

    if power_level < 100:
        return 0

    return int(str(power_level)[-3]) - 5


grid = []
for i in range(grid_size):
    grid.append([])
    for j in range(grid_size):
        grid[i].append(power_level(i, j, serial_number))


max_power = 0
coord = None
size = 0
new_max = 0
for m in range(1, grid_size):
    #print(m)

    for i in range(grid_size):
        if i + m > grid_size:
            break

        for j in range(grid_size):
            if j + m > grid_size:
                break

            try:
                sub_power = sum([sum(grid[i+k][j:j+m]) for k in range(m)])
            except IndexError:
                continue

            new_max += 1
            if sub_power > max_power:
                max_power = sub_power
                coord = (i, j)
                size = m
                #print("New max! {:d} {:d} {:d}".format(i, j, m))
                new_max = 0
                

            if new_max > 300000:
                print(coord, size)
                sys.exit()
                
        
