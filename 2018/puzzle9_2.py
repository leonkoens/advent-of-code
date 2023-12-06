
players = {i: 0 for i in range(476)}
highest = 71431 * 100

marbles = []
current = -1

class Marble:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, marble):
        marble.right = self.right
        marble.left = self

        self.right.left = marble
        self.right = marble


    def delete(self):
        self.right.left = self.left
        self.left.right = self.right

    def __str__(self):
        return str(self.value)


first = Marble(0)
second = Marble(1)
third = Marble(2)
forth = Marble(3)

first.right = third
third.right = second
second.right = forth
forth.right = first

first.left = forth
third.left = first
second.left = third
forth.left = second

current = forth

i = 4

while i < highest:
    
    if i % 23 == 0:
        players[i%len(players)] += i

        for j in range(7):
            current = current.left

        players[i%len(players)] += current.value
        current.delete()
        current = current.right

    else:
        current = current.right
        current.add(Marble(i))
        current = current.right
        
    i += 1

print(max(players.values()))
