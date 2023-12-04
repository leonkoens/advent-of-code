

lines = None
with open('input13.txt') as handle:
    lines = handle.read().split("\n")

grid = []
carts = []
cart_locs = set()

for i, line in enumerate(lines):

    row = []

    for j, c in enumerate(line):
        if c in '<^>v':
            carts.append([i, j, c, 0, 0])
            cart_locs.add((i, j))
            
            if c in '<>':
                row.append('-')
            elif c in '^v':
                row.append('|')
        else:
            row.append(c)

    grid.append(row)

while True:

    if len(cart_locs) == 1:
        print(cart_locs)
        exit()

    carts = sorted(carts, key= lambda item: (item[0], item[1]))

    for cart in carts:
        if cart[4] == 1:
            continue

        x = cart[0]
        y = cart[1]

        if cart[2] == '>':
            y += +1

        elif cart[2] == '<':
            y += -1

        elif cart[2] == '^':
            x += -1

        elif cart[2] == 'v':
            x += +1

        if (x, y) in cart_locs:
            cart[4] = 1
            for search in carts:
                if search[0] == x and search[1] == y:
                    search[4] = 1

            cart_locs.remove((cart[0], cart[1]))
            cart_locs.remove((x, y))
            continue

        cart_locs.remove((cart[0], cart[1]))
        cart_locs.add((x, y))
        cart[0] = x
        cart[1] = y

        new_location = grid[x][y]

        if new_location == '/':

            if cart[2] == '^':
                cart[2] = '>'

            elif cart[2] == '<':
                cart[2] = 'v'

            elif cart[2] == 'v':
                cart[2] = '<'
                
            elif cart[2] == '>':
                cart[2] = '^'

        elif new_location == '\\':

            if cart[2] == '^':
                cart[2] = '<'

            elif cart[2] == '<':
                cart[2] = '^'

            elif cart[2] == 'v':
                cart[2] = '>'
                
            elif cart[2] == '>':
                cart[2] = 'v'

        elif new_location == '+':
            
            if cart[3] % 3 == 0:

                if cart[2] == '^':
                    cart[2] = '<'

                elif cart[2] == '<':
                    cart[2] = 'v'

                elif cart[2] == 'v':
                    cart[2] = '>'
                    
                elif cart[2] == '>':
                    cart[2] = '^'

            elif cart[3] % 3 == 2:

                if cart[2] == '^':
                    cart[2] = '>'

                elif cart[2] == '<':
                    cart[2] = '^'

                elif cart[2] == 'v':
                    cart[2] = '<'
                    
                elif cart[2] == '>':
                    cart[2] = 'v'
            
            cart[3] += 1
