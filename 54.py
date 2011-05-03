def rank(hand):
    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    score = 0
    while True:

        # pair, max score = 24
        # two pair, max score = 36
        pairSet = set()
        pairCount = 0
        max = 0
        for card in hand:
            if card[0] in pairSet:
            pairSet.add(card[0])
        
        # highest card, max score 12
        max = 0
        for card in hand:
            idx = cards.index(card[0])
            if idx > max:
                max = idx
        score = max
    return score

f = open("54.txt", "r").read()
rounds = f.split("\n")
for round in rounds:
    cards = round.split(" ")
    p1 = cards[0:5]
    p2 = cards[5:]
    print p1
    print p2
    print
