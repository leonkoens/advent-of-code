
from collections import Counter
from functools import cmp_to_key


content = None
#with open('7_test.txt', 'r') as handle:
with open('7.txt', 'r') as handle:
    content = [line.strip() for line in handle.readlines()]


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):
        card_order = 'AKQJT98765432'

        def type_score(hand):
            hand_count = Counter(list(hand.split(' ')[0])).values()

            if 5 in hand_count:
                return 7
            if 4 in hand_count:
                return 6
            if 3 in hand_count and 2 in hand_count:
                return 5
            if 3 in hand_count:
                return 4
            if 2 in hand_count:

                if len(hand_count) == 3:
                    return 3
                if len(hand_count) == 4:
                    return 2
            
            return 1

        def compare_hands(a, b):

            a_type_score = type_score(a)
            b_type_score = type_score(b)

            if  a_type_score > b_type_score:
                return 1
            
            if  a_type_score < b_type_score:
                return -1
            
            for i in range(5):

                if a[i] == ' ':
                    break

                a_card_score = 13 - card_order.index(a[i])
                b_card_score = 13 - card_order.index(b[i])
            
                if a_card_score > b_card_score:
                    return 1

                if a_card_score < b_card_score:
                    return -1

            return 1


        hands = sorted(self.content, key=cmp_to_key(compare_hands))

        total = 0
        for i, hand in enumerate(hands):
            total += (i+1) * int(hand.split(' ')[1])

        print(total)


aoc = AdventOfCode(content)
aoc.run()