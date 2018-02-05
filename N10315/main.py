import sys


class Hand:
    HIGH_CARD, PAIR, TWO_PAIRS, THREE_OF_A_KIND, STRAIGHT, \
    FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH = range(1, 10)

    def __init__(self, cards):
        values = [card[0] for card in cards]
        values = [v if v != 'T' else 10 for v in values]
        values = [v if v != 'J' else 11 for v in values]
        values = [v if v != 'Q' else 12 for v in values]
        values = [v if v != 'K' else 13 for v in values]
        values = [v if v != 'A' else 14 for v in values]
        self.values = sorted([int(v) for v in values])
        self.value_counts = {v: self.values.count(v) for v in range(2, 15)}

        suits = [card[1] for card in cards]
        self.suit_counts = {s: suits.count(s) for s in ['C', 'D', 'H', 'S']}

        # Calculate the type of the hand and its associated value
        fns = [self.has_straight_flush, self.has_four_of_a_kind, self.has_full_house,
               self.has_flush, self.has_straight, self.has_three_of_a_kind,
               self.has_two_pairs, self.has_pair, self.has_high_card]
        for fn in fns:
            self.type, self.value = fn()
            if self.type != 0:
                break

    def has_high_card(self):
        return self.HIGH_CARD, max(self.values)

    def has_pair(self):
        pair_values = [k for k, v in self.value_counts.items() if v == 2]
        if pair_values:
            return self.PAIR, pair_values[0]
        return 0, None

    def has_two_pairs(self):
        pair_values = [k for k, v in self.value_counts.items() if v == 2]
        if len(pair_values) == 2:
            return self.TWO_PAIRS, max(pair_values)
        return 0, None

    def has_three_of_a_kind(self):
        for k, v in self.value_counts.items():
            if v == 3:
                return self.THREE_OF_A_KIND, k
        return 0, None

    def has_straight(self):
        if self.are_consecutive():
            return self.STRAIGHT, max(self.values)
        return 0, None

    def has_flush(self):
        if any(v == 5 for v in self.suit_counts.values()):
            return self.FLUSH, max(self.values)
        return 0, None

    def has_full_house(self):
        has_pair, _ = self.has_pair()
        if has_pair:
            for k, v in self.value_counts.items():
                if v == 3:
                    return self.FULL_HOUSE, k
        return 0, None

    def has_four_of_a_kind(self):
        for k, v in self.value_counts.items():
            if v == 4:
                return self.FOUR_OF_A_KIND, k
        return 0, None

    def has_straight_flush(self):
        has_straight, max_val = self.has_straight()
        if has_straight and any(v == 5 for v in self.suit_counts.values()):
            return self.STRAIGHT_FLUSH, max_val
        return 0, None

    def are_consecutive(self):
        values = self.values
        if 2 in values: values = [v if v != 14 else 1 for v in values]
        return values[0] == values[1] - 1 == values[2] - 2 == values[3] - 3 == values[4] - 4


BLACK_WINS = 'Black wins.'
WHITE_WINS = 'White wins.'
TIE = 'Tie.'


def compare_values(black_values, white_values):
    for i in range(len(black_values) - 1, -1, -1):
        if black_values[i] > white_values[i]:
            return BLACK_WINS
        elif white_values[i] > black_values[i]:
            return WHITE_WINS
    return TIE


def solve(black, white):
    if black.type > white.type:
        return BLACK_WINS
    elif white.type > black.type:
        return WHITE_WINS
    else:
        if black.value > white.value:
            return BLACK_WINS
        elif white.value > black.value:
            return WHITE_WINS
        if black.type in [Hand.HIGH_CARD, Hand.PAIR, Hand.FLUSH]:
            return compare_values(black.values, white.values)
        elif black.type == Hand.TWO_PAIRS:
            black_2nd_pair_val = min(k for k, v in black.value_counts.items() if v == 2)
            white_2nd_pair_val = min(k for k, v in white.value_counts.items() if v == 2)
            if black_2nd_pair_val > white_2nd_pair_val:
                return BLACK_WINS
            elif white_2nd_pair_val > black_2nd_pair_val:
                return WHITE_WINS
            else:
                return compare_values(black.values, white.values)
        else:
            return TIE


def main(file):
    res = []
    for line in file:
        split = line.split()
        black, white = Hand(split[:5]), Hand(split[5:])
        res.append(solve(black, white) + '\n')
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
