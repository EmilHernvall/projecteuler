from random import randint, shuffle
from collections import defaultdict

def dice():
    return randint(1,4)

def two_dice():
    return dice(),dice()

squares = [ "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL",
            "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP",
            "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J",
            "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2" ]

def simulate(n):
    cc = [ "GGO", "G2J", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D" ]
    chance = [ "GGO", "G2J", "GC1", "GE3", "GH2", "GR1", "GNR", "GNR", "GNU", "GM3",
               "D", "D", "D", "D", "D", "D" ]

    shuffle(cc)
    shuffle(chance)

    cc_pos, chance_pos = 0, 0

    pos = 0
    freq = defaultdict(int)
    two_equals = 0
    for i in xrange(0, n):
        dice1, dice2 = two_dice()
        dice_roll = dice1 + dice2
        if dice1 == dice2:
            two_equals += 1
        else:
            two_equals = 0

        if two_equals == 3:
            pos = squares.index("JAIL")
            two_equals = 0
        else:
            pos = (pos + dice_roll) % len(squares)

        if squares[pos] == "JAIL":
            pass
        elif squares[pos].startswith("CC"):
            card = cc[cc_pos]
            cc_pos += 1
            if cc_pos == len(cc):
                cc_pos = 0

            if card == "GGO": pos = squares.index("GO")
            elif card == "G2J":
                two_equals = 0
                pos = squares.index("JAIL")
        elif squares[pos].startswith("CH"):
            card = chance[chance_pos]
            chance_pos += 1
            if chance_pos == len(chance):
                chance_pos = 0

            if card == "GGO": pos = squares.index("GO")
            elif card == "G2J":
                two_equals = 0
                pos = squares.index("JAIL")
            elif card == "GC1": pos = squares.index("C1")
            elif card == "GE3": pos = squares.index("E3")
            elif card == "GH2": pos = squares.index("H2")
            elif card == "GR1": pos = squares.index("R1")
            elif card == "GNR":
                while not squares[pos].startswith("R"):
                    pos = (pos + 1) % len(squares)
            elif card == "GNU":
                while not squares[pos].startswith("U"):
                    pos = (pos + 1) % len(squares)
            elif card == "GM3":
                pos -= 3
                if pos < 0: pos += len(squares)
        elif squares[pos] == "G2J":
            two_equals = 0
            pos = squares.index("JAIL")

        freq[pos] += 1

    res = sorted([(k, squares[k], 100*v/float(n)) for k, v in freq.items()], key=lambda x: x[2], reverse=True)
    print res
    print "".join(["%02d" % (nr,) for nr, name, freq in res[0:3]])

simulate(100000)
