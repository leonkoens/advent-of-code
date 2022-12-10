
content = None
with open('9.txt', 'r') as handle:
    content = handle.readlines()


#content = """
#R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2
#""".strip().split("\n")

#content = """
#R 5
#U 8
#L 8
#D 3
#R 17
#D 10
#L 25
#U 20
#""".strip().split("\n")

grid_map_1 = {}
grid_map_2 = {}
snake_length = 10
snake = [[0, 0] for i in range(snake_length)]

for line in content:
    direction, steps = line.split(' ')

    for i in range(int(steps)):

        if direction == 'U':
            snake[0][1] -= 1
        if direction == 'R':
            snake[0][0] += 1
        if direction == 'D':
            snake[0][1] += 1
        if direction == 'L':
            snake[0][0] -= 1

        for j in range(1, snake_length):

            x_diff = snake[j][0] - snake[j-1][0]
            y_diff = snake[j][1] - snake[j-1][1]

            if abs(x_diff) == 2 and abs(y_diff) == 2 or abs(x_diff) == 2 and abs(y_diff) == 1 or abs(y_diff) == 2 and abs(x_diff) == 1:
                snake[j][0] = snake[j][0] + 1 if x_diff < 0 else snake[j][0] - 1
                snake[j][1] = snake[j][1] + 1 if y_diff < 0 else snake[j][1] - 1
            elif abs(x_diff) == 2:
                snake[j][0] = snake[j][0] + 1 if x_diff < 0 else snake[j][0] - 1
            elif abs(y_diff) == 2:
                snake[j][1] = snake[j][1] + 1 if y_diff < 0 else snake[j][1] - 1

        grid_map_1[snake[1][0], snake[1][1]] = 1
        grid_map_2[snake[-1][0], snake[-1][1]] = 1

print("Part 1", len(grid_map_1))
print("Part 2", len(grid_map_2))

