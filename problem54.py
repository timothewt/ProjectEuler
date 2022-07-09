import collections

# hands values : royal flush = 9; straight flush = 8; Four of a kind = 7; Full house = 6; Flush = 5; Straight = 4;
#                Three of a kind = 3; Two pairs = 2; Single pair = 1; High card = 0
# 2..10 = 2..10; J, Q, K, Ace = 11, 12, 13, 14


def flush(hand):
    return hand[0][-1:] == hand[1][-1:] == hand[2][-1:] == hand[3][-1:] == hand[4][-1:]


def four_of_a_kind(hand):
    count = [count for item, count in collections.Counter([int(card[:-1]) for card in hand]).items()]
    items = [item for item, count in collections.Counter([int(card[:-1]) for card in hand]).items()]
    if count == [4, 1] or count == [1, 4]:
        return [True, items[0] if count == [4, 1] else items[1], items[1] if count == [4, 1] else items[0]]
    return [False, 0, 0]


def full_house(hand):
    count = [count for item, count in collections.Counter([int(card[:-1]) for card in hand]).items()]
    items = [item for item, count in collections.Counter([int(card[:-1]) for card in hand]).items()]
    if count == [3, 2] or count == [2, 3]:
        return [True, items[0] if count == [3, 2] else items[1]]
    return [False, 0]


def royal_flush(hand):
    return hand[0] == 10 and hand[1] == 11 and hand[2] == 12 and hand[3] == 13 and hand[4] == 14


def hand_value(hand: str):
    # hand : '5H 5C 6S 7S KD'
    # returns [hand value, card values in the hand, highest card]
    hand = hand.replace('A', '14').replace('K', '13').replace('Q', '12').replace('J', '11').split()
    if four_of_a_kind(hand)[0]:  # checks for a four of a kind
        return [7, four_of_a_kind(hand)[1], four_of_a_kind(hand)[2]]
    if flush(hand):
        hand = [int(card[:-1]) for card in hand]
        hand.sort()
        if royal_flush(hand):
            return [9, 14, 14]

    return hand


print(hand_value('5H 5C KD 7S 6S'))
print(hand_value('10C AC KC QC JC'))
print(hand_value('8C 5H 5H 5S 5D'))