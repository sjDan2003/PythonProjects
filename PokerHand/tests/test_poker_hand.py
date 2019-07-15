import unittest
from main import main, PokerHand


class PokerHandTestClass(unittest.TestCase):

    def poker_hand_tester(self, test_hand_string, test_hand_type):

        poker_hand = PokerHand(test_hand_string)
        return_hand_type = poker_hand.determine_poker_hand()
        self.assertEqual(return_hand_type, test_hand_type,
                         '{} should be a {}'.format(test_hand_string,
                                                    test_hand_type))

    def test_is_royal_flush(self):

        test_hand_string = '10H JH QH KH AH'
        test_hand_type = 'Royal Flush'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_straight_flush(self):

        test_hand_string = '2H 3H 4H 5H 6H'
        test_hand_type = 'Straight Flush'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_full_house(self):

        test_hand_string = '2H 2D 2S 3H 3D'
        test_hand_type = 'Full House'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_flush(self):

        test_hand_string = '4S JS 10S 2S 9S'
        test_hand_type = 'Flush'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_straight(self):

        test_hand_string = '9S 8D 7S 6D 5H'
        test_hand_type = 'Straight'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_three_of_a_kind(self):

        test_hand_string = '7S 7D 7C KS 3S'
        test_hand_type = 'Three Of A Kind'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_two_pair(self):

        test_hand_string = '4C 4D 3S 3D QS'
        test_hand_type = 'Two Pair'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_pair(self):

        test_hand_string = 'AH AD 8C 4S 7H'
        test_hand_type = 'Pair'
        self.poker_hand_tester(test_hand_string, test_hand_type)

    def test_is_high_card(self):

        test_hand_string = '3D JS 8C 4H 2S'
        test_hand_type = 'High Card'
        self.poker_hand_tester(test_hand_string, test_hand_type)
