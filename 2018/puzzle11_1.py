
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
for i in range(grid_size):
    for j in range(grid_size):

        try:
            sub_power = sum([sum(grid[i+k][j:j+3]) for k in range(3)])
        except IndexError:
            continue
            
        if sub_power > max_power:
            max_power = sub_power
            coord = (i, j)

print(coord)
                
        
