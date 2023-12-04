
players = {i: 0 for i in range(476)}
highest = 71431

marbles = []
current = -1

i = 0

while i < highest:

    
    if len(marbles) < 2:
        marbles.append(i)
        current += 1

    elif len(marbles) == 2:
        marbles.insert(1, i)
        current = 1
        
    else:
        if i % 23 == 0:
            players[i%len(players)] += i
            current = (current - 7) % len(marbles)



            players[i%len(players)] += marbles[current]

            del marbles[current]

        else:

            current = (current + 2) % len(marbles)

            if current == 0:
                marbles.append(i)
                current = len(marbles)-1

            else:
                marbles.insert(current, i)


    i += 1

print(max(players.values()))
