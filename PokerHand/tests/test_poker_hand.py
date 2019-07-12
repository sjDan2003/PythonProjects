import unittest
from main import PokerHand


class PokerHandTestClass(unittest.TestCase):

    def test_get_card_suit(self):

        test_poker_hand_string = '5H AS 5C 4D AC'
        poker_hand = PokerHand(test_poker_hand_string)
        suit = poker_hand._get_card_suit(0)
        expected_suit = 'H'
        self.assertEqual(suit, expected_suit, 'Expected a Heart')

    def test_get_card_value(self):

        test_poker_hand_string = '5H AS 5C 4D AC'
        poker_hand = PokerHand(test_poker_hand_string)
        suit = poker_hand._get_card_value(0)
        expected_suit = '5'
        self.assertEqual(suit, expected_suit, 'Expected a 5')
