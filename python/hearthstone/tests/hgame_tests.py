import unittest
from src.model.hgame import Druid, Hunter, Mage, Paladin, Priest, \
                            Rogue, Shaman, Warlock, Warrior, AllHeroes, init, drawCard, drawNCards
from src.model.testdata import AcidicSwampOoze, AncestralHealing

class TestHGame(unittest.TestCase):

    def setUp(self):
        self.model = init()

    def test_hero_models(self):
        self.assertEquals(0, Druid[1])
        self.assertEquals(1, Hunter[1])
        self.assertEquals(2, Mage[1])
        self.assertEquals(3, Paladin[1])
        self.assertEquals(4, Priest[1])
        self.assertEquals(5, Rogue[1])
        self.assertEquals(6, Shaman[1])
        self.assertEquals(7, Warlock[1])
        self.assertEquals(8, Warrior[1])

        for hero in AllHeroes:
            self.assertEquals((30, 0), hero[0])


    def test_init(self):
        self.assertEquals((Druid, Paladin), self.model[0])
        self.assertEquals(
            ([AcidicSwampOoze, AcidicSwampOoze, AcidicSwampOoze], [AcidicSwampOoze, AcidicSwampOoze, AcidicSwampOoze, AcidicSwampOoze]),
            self.model[1])
        self.assertEquals(27, len(self.model[2][0])) #Player1 has 27 cards in deck
        self.assertEquals(26, len(self.model[2][1])) #Player2 has 26 cards in deck
        self.assertEquals(([],[]), self.model[3])
        self.assertEquals(0, self.model[4])

    def test_drawCard(self):
        test_deck = self.model[2][0]
        test_hand = self.model[1][0]
        top_card = test_deck[0]

        new_deck_hand = drawCard(test_deck, test_hand)
        actual_deck = new_deck_hand[1]
        actual_hand = new_deck_hand[0]

        self.assertFalse(len(test_hand) == 10)
        self.assertFalse(len(test_deck) == 0)#Validate test data

        self.assertEquals(len(test_hand) + 1, len(actual_hand)) #One more card
        self.assertEquals(top_card, actual_hand[len(actual_hand) - 1])#Card is from topdeck
        self.assertTrue(top_card in actual_hand)#Card is from topdeck

    def test_drawNCards(self):
        test_deck = self.model[2][0]
        test_hand = self.model[1][0]
        numCards = 3
        top_cards = test_deck[0:numCards + 1]


        new_deck_hand = drawNCards(test_deck, test_hand, numCards)
        actual_deck = new_deck_hand[1]
        actual_hand = new_deck_hand[0]
        print(len(test_hand))
        self.assertFalse(len(test_hand) >= (10 - numCards))
        self.assertFalse(len(test_deck) <= numCards + 1)#Validate test data

        self.assertEquals(len(test_hand) + numCards, len(actual_hand)) #One more card
        self.assertEquals(len(test_deck) - numCards, len(actual_deck))


        for card in top_cards:
            self.assertTrue(card in actual_hand)



