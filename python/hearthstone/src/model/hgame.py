from typing import Dict, Tuple, List, NewType, Union
from src.model.testdata import *
from src.model.Types import *



def isFirstPlayerTurn(model : HearthstoneModel) -> bool:
    turnNo = model[4]
    return turnNo % 2 == 0


def playerHasLethal(model : HearthstoneModel, isFirstPlayerTurn : bool):
    return False


def getSampleDeck(hero : Hero) -> Deck:
    if type(hero) is Druid:
        return druidSampleDeck
    else:
        return paladinSampleDeck

def drawOpeningHand(deck : Deck, isFirstPlayer : bool) -> Tuple[Hand, Deck]:
    if isFirstPlayer:
        #hand is empty at beginning of game
        return drawNCards(deck, [], 3)
    else:
        return drawNCards(deck, [], 4)

def drawNCards(deck : Deck, currentHand : Hand, n : int) -> Tuple[Hand, Deck]:
    return drawNCardsAccum(deck, currentHand, n, 0)

def drawNCardsAccum(deck : Deck, currentHand : Hand, n : int, acc : int) -> Tuple[Hand, Deck]:
    if n == acc:
        return (currentHand, deck)
    else:
        deck_hand_after_draw = drawCard(deck, currentHand)
        newhand = deck_hand_after_draw[0]
        newdeck = deck_hand_after_draw[1]
        return drawNCardsAccum(newdeck, newhand, n, acc + 1)

def drawCard(deck : Deck, currentHand : Hand) -> Tuple[Hand, Deck]:
    newDeck = deck.copy()
    newHand = currentHand.copy()

    if len(deck) == 0:
        pass  # TODO: subtract -x health for no card penalty
    else:
        topCard = deck[0]
        if not len(currentHand) == 10:
            finalHand = newHand + [topCard]
            newDeck = deck[1:]
            return (finalHand, newDeck)

def init() -> HearthstoneModel:
    first_player = Druid
    second_player = Paladin
    first_deck_init = getSampleDeck(first_player)
    second_deck_init = getSampleDeck(second_player)

    first_hand_deck = drawOpeningHand(first_deck_init, True)
    first_hand = first_hand_deck[0]
    first_deck = first_hand_deck[1]
    second_hand_deck = drawOpeningHand(second_deck_init, False)
    second_hand = second_hand_deck[0]
    second_deck = second_hand_deck[1]

    return HearthstoneModel(
        (
            (first_player, second_player),
            (first_hand, second_hand),
            (first_deck, second_deck),
            ([], []), #No minions on board
            TurnNumber(0)
        )
    )



def determineBestTurn(model : HearthstoneModel, firstPlayerTurn : bool) -> (Turn, HearthstoneModel):
    pass

#Runs a simulation of the game and returns whether the first player to move wins
def runSimulation(model : HearthstoneModel) -> bool:
    firstPlayerTurn = isFirstPlayerTurn(model)
    if playerHasLethal(model, firstPlayerTurn):
        return firstPlayerTurn
    else:
        turnAndGameState = determineBestTurn(model, firstPlayerTurn)
        movesPlayed = turnAndGameState[0]
        nextGameState = turnAndGameState[1]
        return runSimulation(nextGameState)

def main():
    runSimulation(init())




if __name__ == '__main__':
    main()

