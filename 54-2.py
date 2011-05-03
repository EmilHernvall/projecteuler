class RoyalFlush(object):

	def __init__(self):
		pass

	def handName(self):
		return "Royal Flush"

	def isHand(self, hand):
		ten, jack, queen, king, ace = False, False, False, False, False
		suite = hand[0][1]
		for card in hand:
			if card[0] == "T":
				ten = True
			elif card[0] == "J":
				jack = True
			elif card[0] == "Q":
				queen = True
			elif card[0] == "K":
				king = True
			elif card[0] == "A":
				ace = True
			else:
				return False

			if card[1] != suite:
				return False

		return ten and jack and queen and king and ace

	def cmp(self, hand1, hand2):
		return 0

class StraightFlush(object):

	def __init__(self):
		pass

	def handName(self):
		return "Straigth Flush"

	def isHand(self, hand):
		cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

		ranks = []
		for card in hand:
			ranks.append(card[0])
		ranks.sort()

		isStraight = False
		for i in range(0, len(cards) - len(ranks) + 1):
			cmp = cards[i:i+5]
			cmp.sort()
#			print cmp
			if cmp == ranks:
				isStraight = True
				break

		if not isStraight:
			return False

		suite = hand[0][1]
		for card in hand:
			if card[1] != suite:
				return False

		return True

	def cmp(self, hand1, hand2):
		return 0

class FourOfAKind(object):

	def __init__(self):
		pass

	def handName(self):
		return "Four Of A Kind"

	def isHand(self, hand):
		ranks = []
		for card in hand:
			ranks.append(card[0])

		uniqueRanks = set(ranks)

		return len(uniqueRanks) == 2

	def cmp(self, hand1, hand2):
		return 0

class FullHouse(object):

	def __init__(self):
		pass

	def handName(self):
		return "Full House"

	def isHand(self, hand):
		counts = {}
		for card in hand:
			rank = card[0]

			if counts.has_key(rank):
				counts[rank] += 1
			else:
				counts[rank] = 1

		two = False
		three = False
		for c in counts.itervalues():
			if c == 2:
				two = True
			elif c == 3:
				three = True

		return two and three

	def cmp(self, hand1, hand2):
		return 0

class Flush(object):

	def __init__(self):
		pass

	def handName(self):
		return "Flush"

	def isHand(self, hand):
		suite = hand[0][1]
		for card in hand:
			if card[1] != suite:
				return False

		return True

	def cmp(self, hand1, hand2):
		return 0

class Straight(object):

	def __init__(self):
		pass

	def handName(self):
		return "Straigth"

	def isHand(self, hand):
		cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

		ranks = []
		for card in hand:
			ranks.append(card[0])
		ranks.sort()

		isStraight = False
		for i in range(0, len(cards) - len(ranks) + 1):
			cmp = cards[i:i+5]
			cmp.sort()
			if cmp == ranks:
				isStraight = True
				break

		if not isStraight:
			return False

		return True

	def cmp(self, hand1, hand2):
		return 0

class ThreeOfAKind(object):

	def __init__(self):
		pass

	def handName(self):
		return "Three Of A Kind"

	def isHand(self, hand):
		counts = {}
		for card in hand:
			rank = card[0]

			if counts.has_key(rank):
				counts[rank] += 1
			else:
				counts[rank] = 1

		twoCount = 0
		for c in counts.itervalues():
			if c == 3:
				return True

		return False

	def cmp(self, hand1, hand2):
		return 0

class TwoPair(object):

	def __init__(self):
		pass

	def handName(self):
		return "Two Pair"

	def isHand(self, hand):
		counts = {}
		for card in hand:
			rank = card[0]

			if counts.has_key(rank):
				counts[rank] += 1
			else:
				counts[rank] = 1

		twoCount = 0
		for c in counts.itervalues():
			if c == 2:
				twoCount += 1

		return twoCount == 2

	def cmp(self, hand1, hand2):
		return 0

class OnePair(object):

	def __init__(self):
		pass

	def handName(self):
		return "One Pair"

	def isHand(self, hand):
		ranks = []
		for card in hand:
			ranks.append(card[0])

		uniqueRanks = set(ranks)

		return len(uniqueRanks) == 4

	def cmp(self, hand1, hand2):
		counts = {}
		for card in hand1:
			rank = card[0]

			if counts.has_key(rank):
				counts[rank] += 1
			else:
				counts[rank] = 1

		p1rank = ""
		for k, v in counts.iteritems():
			if v == 2:
				p1rank = k

		counts = {}
		for card in hand2:
			rank = card[0]

			if counts.has_key(rank):
				counts[rank] += 1
			else:
				counts[rank] = 1

		p2rank = ""
		for k, v in counts.iteritems():
			if v == 2:
				p2rank = k


		cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

		for i, card in enumerate(cards):
			if card == p1rank:
				p1max = i
				break

		for i, card in enumerate(cards):
			if card == p2rank:
				p2max = i
				break

		if p1max > p2max:
			return 1
		elif p2max > p1max:
			return 2
		else:
			return 0		

class HighCard(object):

	def __init__(self):
		pass

	def handName(self):
		return "High Card"

	def isHand(self, hand):
		return True

	def cmp(self, hand1, hand2):
		cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

		p1max = 0
		for card in hand1:
			for i, refCard in enumerate(cards):
				if refCard == card[0]:
					p1max = max(p1max, i)

		p2max = 0
		for card in hand2:
			for i, refCard in enumerate(cards):
				if refCard == card[0]:
					p2max = max(p2max, i)

		if p1max > p2max:
			return 1
		elif p2max > p1max:
			return 2
		else:
			return 0

rf = RoyalFlush()
sf = StraightFlush()
foak = FourOfAKind()
fh = FullHouse()
f = Flush()
s = Straight()
toak = ThreeOfAKind()
tp = TwoPair()
op = OnePair()
hc = HighCard()

#print rf.isHand(["5H", "6H", "7H", "8H", "9H"])
#print rf.isHand(["TH", "JH", "QH", "KH", "AH"])

#print sf.isHand(["9H", "6H", "7H", "8H", "5H"])
#print sf.isHand(["TH", "JH", "QH", "KH", "9H"])

hands = [rf, sf, foak, fh, f, s, toak, tp, op, hc]

f = open("54.txt", "r").read()
rounds = f.split("\n")
p1count, p2count = 0, 0
for round in rounds:
	cards = round.strip().split(" ")
	if len(cards) != 10:
		break

	p1 = cards[0:5]
	p2 = cards[5:]

	p1hand = 0
	p2hand = 0

	print p1
	for i, hand in enumerate(hands):
		if hand.isHand(p1):
			print hand.handName()
			p1hand = i
			break

	print p2
	for i, hand in enumerate(hands):
		if hand.isHand(p2):
			print hand.handName()
			p2hand = i
			break

	if p1hand < p2hand:
		print "p1 wins!"
		p1count += 1
	elif p2hand < p1hand:
		print "p2 wins!"
		p2count += 1
	else:
		hand = hands[p1hand]
		res = hand.cmp(p1, p2)
		if res == 1:
			print "p1 wins!"
			p1count += 1
		elif res == 2:
			print "p2 wins!"
			p2count += 1
		else:
			print "tie!"

	print

print "p1: " + str(p1count)
print "p2: " + str(p2count)
