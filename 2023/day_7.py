import collections
import functools
from enum import Enum

import helpers

class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Card1(Enum):
    _2 = 1
    _3 = 2
    _4 = 3
    _5 = 4
    _6 = 5
    _7 = 6
    _8 = 7
    _9 = 8
    T = 9
    J = 10
    Q = 11
    K = 12
    A = 13


class Card2(Enum):
    J = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    T = 10
    Q = 11
    K = 12
    A = 13


n_of_a_kind = {
    HandType.HIGH_CARD: 1,
    HandType.ONE_PAIR: 2,
    HandType.THREE_OF_A_KIND: 3,
    HandType.FOUR_OF_A_KIND: 4,
    HandType.FIVE_OF_A_KIND: 5
}

n_of_a_kind_inv = {
    1: HandType.HIGH_CARD,
    2: HandType.ONE_PAIR,
    3: HandType.THREE_OF_A_KIND,
    4: HandType.FOUR_OF_A_KIND,
    5: HandType.FIVE_OF_A_KIND
}


def get_hand_type(hand, transform):
    hand_counter = collections.Counter(hand)
    hand_type = None
    match len(hand_counter):
        case 5:
            hand_type = HandType.HIGH_CARD
        case 4:
            hand_type = HandType.ONE_PAIR
        case 3:
            if hand_counter.most_common(1)[0][1] == 2:
                hand_type = HandType.TWO_PAIR
            else:
                hand_type = HandType.THREE_OF_A_KIND
        case 2:
            if hand_counter.most_common(1)[0][1] == 3:
                hand_type = HandType.FULL_HOUSE
            else:
                hand_type = HandType.FOUR_OF_A_KIND
        case 1:
            hand_type = HandType.FIVE_OF_A_KIND

    if transform and "J" in hand:
        jokers = hand_counter['J']
        match hand_type:
            case HandType.HIGH_CARD | HandType.ONE_PAIR | HandType.THREE_OF_A_KIND | HandType.FOUR_OF_A_KIND:
                try:
                    if n_of_a_kind[hand_type] == jokers:
                        hand_type = n_of_a_kind_inv[n_of_a_kind[hand_type] + 1]
                    else:
                        hand_type = n_of_a_kind_inv[n_of_a_kind[hand_type] + jokers]
                except KeyError:
                    hand_type = HandType.FIVE_OF_A_KIND
            case HandType.TWO_PAIR:
                if jokers == 1:
                    hand_type = HandType.FULL_HOUSE
                else:
                    hand_type = n_of_a_kind_inv[n_of_a_kind[HandType.ONE_PAIR] + jokers]
            case HandType.FULL_HOUSE:
                if jokers == 1:
                    hand_type = HandType.FOUR_OF_A_KIND
                else:
                    hand_type = HandType.FIVE_OF_A_KIND

    return hand_type


class HandComparer(object):
    def __init__(self, part):
        self.part = part

        if part == 1:
            self.card_enum = Card1
        else:
            self.card_enum = Card2

    def get_hand_type(self, hand):
        return get_hand_type(hand, self.part == 2)

    def compare_hands(self, hand1, hand2):
        hand_comparison = self.get_hand_type(hand1).value - self.get_hand_type(hand2).value
        if hand_comparison != 0:
            return hand_comparison
        for i, card in enumerate(hand1):
            try:
                int(card)
                c1 = "_" + card
            except ValueError:
                c1 = card
            try:
                int(hand2[i])
                c2 = "_" + hand2[i]
            except ValueError:
                c2 = hand2[i]
            card_comparison = self.card_enum[c1].value - self.card_enum[c2].value
            if card_comparison != 0:
                return card_comparison
        return 0


def part_one(puzzle_input):
    hand_comparer = HandComparer(1)
    sorted_hands = sorted(list(puzzle_input.keys()), key=functools.cmp_to_key(hand_comparer.compare_hands))
    res = 0
    for i, hand in enumerate(sorted_hands):
        res += (i + 1) * puzzle_input[hand]
    return res


def part_two(puzzle_input):
    hand_comparer = HandComparer(2)
    sorted_hands = sorted(list(puzzle_input.keys()), key=functools.cmp_to_key(hand_comparer.compare_hands))
    res = 0
    for i, hand in enumerate(sorted_hands):
        res += (i + 1) * puzzle_input[hand]
    return res


loaded_puzzle_input = helpers.load_puzzle_input(2023, 7)
# loaded_puzzle_input = helpers.load_test_puzzle_input()
parsed = {hand[0]: int(hand[1]) for hand in list(map(lambda x: x.split(' '), loaded_puzzle_input))}
# print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))