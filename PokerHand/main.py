import argparse


class PokerHand:

    _CARD_VALUE_INDEX = 0
    _CARD_SUIT_INDEX = 1

    def __init__(self, cards):

        self._cards = cards.split(' ')

    def _get_card_value(self, card_index):

        return self._cards[card_index][self._CARD_VALUE_INDEX]

    def _get_card_suit(self, card_index):

        return self._cards[card_index][self._CARD_SUIT_INDEX]

    def _is_same_suit(self):

        suit_to_check = _get_card_suit(0)
        for card_index in range(1, len(self._cards)):
            if _get_card_suit(card_index) != suit_to_check:
                return False
        return True

    def _is_royal_flush(self):

        # Check to see if the card values are consecutive 10 and above
        # Check to see if all cards are of the same type
        pass

    def _is_straight_flush(self):

        # Check to see if all cards are of the same type
        pass

    def _is_four_of_a_kind(self):
        pass

    def _is_full_house(self):
        pass

    def _is_flush(self):
        pass

    def _is_straight(self):
        pass

    def _is_three_of_a_kind(self):
        pass

    def _is_two_pair(self):
        pass

    def _is_pair(self):
        pass

    def _is_high_card(self):
        return 'High Card'

    def determine_poker_hand(self):

        is_poker_hand_array = [_is_royal_flush, _is_straight_flush, _is_four_of_a_kind, _is_full_house,
                               _is_flush, _is_straight, _is_three_of_a_kind, _is_two_pair, _is_pair,
                               _is_high_card]

        for is_poker_hand in poker_hand_array:

            is_hand_true, hand_type = is_poker_hand()
            if is_hand_true is True:
                print(hand_type)


def get_filename_from_user():

    parser = argparse.ArgumentParser(description='Converts a roman numeral to a decimal value')
    parser.add_argument('--filename', dest='filename', required=True)
    args = parser.parse_args()

    return args.filename


def main():

    filename = get_filename_from_user()
    test_hand = '5H AS 5C 4D AC'
    user_hand = PokerHand(test_hand)
    user_hand.determine_poker_hand()

if __name__ == "__main__":
    main()
