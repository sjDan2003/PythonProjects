#!/usr/bin/env python3

import argparse


class PokerHand:

    _CARD_VALUE_INDEX = 0
    _CARD_SUIT_INDEX = 1
    _FIRST_TWO_PAIR_INDEX = 0
    _SECOND_TWO_PAIR_INDEX = 1
    _TOTAL_NUMBER_OF_SUITS = 4
    _LARGEST_SUIT_COUNT_INDEX = _TOTAL_NUMBER_OF_SUITS - 1

    def __init__(self, cards_string):

        self._initialize_values()
        self._convert_card_string_to_card_array(cards_string)
        self._get_number_of_suits()
        self._sort_cards_by_value()
        self._check_for_pairs()

    def _initialize_values(self):

        self._card_suit_breakdown = []
        self._cards = []
        self._is_pair_flags = [False, False]
        self._is_three_of_a_kind_flag = False
        self._is_four_of_a_kind_flag = False

    def _convert_card_string_to_card_array(self, cards_string):

        card_value_lookup_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                                  '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
                                  'Q': 12, 'K': 13, 'A': 14}

        def _get_value_from_string(self, card):

            card_value = 0
            if len(card) == len('10') + 1:
                card_value = card_value_lookup_dict['10']
            else:
                card_value_str = card[self._CARD_VALUE_INDEX]
                card_value = card_value_lookup_dict[card_value_str]
            return card_value

        def _get_suit_from_string(self, card):

            if len(card) == len('10') + 1:
                return card[self._CARD_SUIT_INDEX + 1]
            else:
                return card[self._CARD_SUIT_INDEX]

        for card in cards_string.split(' '):
            card_value = _get_value_from_string(self, card)
            card_suit = _get_suit_from_string(self, card)
            self._cards.append([card_value, card_suit])

    def _get_number_of_suits(self):

        card_suit_breakdown_dictionary = {'H': 0, 'D': 0, 'S': 0, 'C': 0}
        for card in self._cards:
            suit = card[self._CARD_SUIT_INDEX]
            card_suit_breakdown_dictionary[suit] = card_suit_breakdown_dictionary[suit] + 1

        self._card_suit_breakdown = sorted(card_suit_breakdown_dictionary.values())

    def _get_card_value(self, card_index):

        return self._cards[card_index][self._CARD_VALUE_INDEX]

    def _get_card_suit(self, card_index):

        return self._cards[card_index][self._CARD_SUIT_INDEX]

    def _is_same_suit(self):

        is_same_suit = False
        if self._card_suit_breakdown[self._LARGEST_SUIT_COUNT_INDEX] == len(self._cards):
            is_same_suit = True
        return is_same_suit

    def _update_pair_flags(self, is_pair,
                           is_three_of_a_kind,
                           is_four_of_a_kind):

        if is_four_of_a_kind:
            self._is_four_of_a_kind_flag = True
        elif is_three_of_a_kind:
            self._is_three_of_a_kind_flag = True
        elif is_pair:
            if not self._is_pair_flags[self._FIRST_TWO_PAIR_INDEX]:
                self._is_pair_flags[self._FIRST_TWO_PAIR_INDEX] = True
            else:
                self._is_pair_flags[self._SECOND_TWO_PAIR_INDEX] = True

    def _check_for_pairs(self):

        is_pair = False
        is_three_of_a_kind = False
        is_four_of_a_kind = False

        for card_index in range(0, len(self._cards) - 1):

            if self._get_card_value(card_index) == \
               self._get_card_value(card_index + 1):

                if not is_pair:
                    is_pair = True
                elif not is_three_of_a_kind:
                    is_three_of_a_kind = True
                elif not is_four_of_a_kind:
                    is_four_of_a_kind = True
            else:
                self._update_pair_flags(is_pair,
                                        is_three_of_a_kind,
                                        is_four_of_a_kind)
                is_pair = False
                is_three_of_a_kind = False
                is_four_of_a_kind = False

        self._update_pair_flags(is_pair, is_three_of_a_kind, is_four_of_a_kind)

    def _swap_cards(self, swap_index_1, swap_index_2):

        self._cards[swap_index_1], self._cards[swap_index_2] = \
            self._cards[swap_index_2], self._cards[swap_index_1]

    def _sort_cards_by_value(self):

        for curr_card_index in range(0, len(self._cards)):

            smallest_value_index = curr_card_index
            for next_card_index in range(curr_card_index + 1, len(self._cards)):
                if self._get_card_value(next_card_index) < \
                   self._get_card_value(smallest_value_index):
                    smallest_value_index = next_card_index

            if smallest_value_index != curr_card_index:
                self._swap_cards(smallest_value_index, curr_card_index)

    def _is_hand_sequential(self):

        for card_index in range(0, len(self._cards) - 1):

            next_card_index = card_index + 1
            if self._get_card_value(next_card_index) != \
               (self._get_card_value(card_index) + 1):
                return False

        return True

    def _is_royal_flush(self):

        ROYAL_FLUSH_LOWEST_CARD = 10
        if self._is_same_suit() and \
           self._get_card_value(0) == ROYAL_FLUSH_LOWEST_CARD and \
           self._is_hand_sequential():

            return 'Royal Flush'

        else:
            return None

    def _is_straight_flush(self):

        if self._is_same_suit() and \
           self._is_hand_sequential():
            return 'Straight Flush'
        else:
            return None

    def _is_four_of_a_kind(self):

        if self._is_four_of_a_kind_flag:
            return 'Four Of A Kind'
        else:
            return None

    def _is_full_house(self):
        if self._is_three_of_a_kind_flag and \
           self._is_pair_flags[self._FIRST_TWO_PAIR_INDEX]:
            return 'Full House'
        else:
            return None

    def _is_flush(self):

        if self._is_same_suit():
            return 'Flush'
        else:
            return None

    def _is_straight(self):

        if self._is_hand_sequential():
            return 'Straight'
        else:
            return None

    def _is_three_of_a_kind(self):

        if self._is_three_of_a_kind_flag:
            return 'Three Of A Kind'
        else:
            return None

    def _is_two_pair(self):

        if self._is_pair_flags[self._FIRST_TWO_PAIR_INDEX] and \
           self._is_pair_flags[self._SECOND_TWO_PAIR_INDEX]:
            return 'Two Pair'
        else:
            return None

    def _is_pair(self):

        if self._is_pair_flags[self._FIRST_TWO_PAIR_INDEX]:
            return 'Pair'

    def _is_high_card(self):

        return 'High Card'

    def determine_poker_hand(self):

        poker_hand_array = [self._is_royal_flush, self._is_straight_flush,
                            self._is_four_of_a_kind, self._is_full_house,
                            self._is_flush, self._is_straight, self._is_three_of_a_kind,
                            self._is_two_pair, self._is_pair, self._is_high_card]

        for is_poker_hand in poker_hand_array:

            hand_type = is_poker_hand()
            if hand_type is not None:
                return hand_type


def get_filename_from_user():

    program_description = 'Calculates the rank of a poker hand'
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('--filename', dest='filename', required=True)
    args = parser.parse_args()

    return args.filename


def main():

    filename = get_filename_from_user()

    with open(filename, 'r') as input_file:

        for poker_hand in input_file:
            user_hand = PokerHand(poker_hand.strip())
            hand_type = user_hand.determine_poker_hand()
            print(hand_type)

if __name__ == "__main__":
    main()
