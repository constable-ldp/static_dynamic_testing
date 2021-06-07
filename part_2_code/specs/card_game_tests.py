import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('diamonds', 1)
        self.card2 = Card('hearts', 7)
        self.card_game = CardGame()

    def test_card_has_suit(self):
        self.assertEqual('diamonds', self.card1.suit)
        
    def test_card_has_value(self):
        self.assertEqual(7, self.card2.value)

    def test_can_find_ace(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)
    
    def test_can_not_find_ace(self):
        outcome = self.card_game.check_for_ace(self.card2)
        self.assertEqual(False, outcome)
    
    def test_can_find_highest_card_by_value(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(result, self.card2)
    
    def test_can_find_total_value_of_cards(self):
        cards = [self.card1, self.card2]
        result = self.card_game.cards_total(cards)
        self.assertEqual(result, 'You have a total of 8')