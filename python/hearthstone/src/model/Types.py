from typing import Tuple, List, NewType, Union

Effect = NewType('Effect', None)#TODO: implement effect
Target = NewType('Target', None)#TODO: implement target

Hero = NewType('Hero', Tuple[Tuple[int, int], int]) #((Health, Armor), HeroNumber)
Druid = Hero(((30, 0), 0))
Hunter = Hero(((30, 0), 1))
Mage = Hero(((30, 0), 2))
Paladin = Hero(((30, 0), 3))
Priest = Hero(((30, 0), 4))
Rogue = Hero(((30, 0), 5))
Shaman = Hero(((30, 0), 6))
Warlock = Hero(((30, 0), 7))
Warrior = Hero(((30, 0), 8))
AllHeroes = [Druid, Hunter, Mage, Paladin, Priest, Rogue, Shaman, Warlock, Warrior]


DruidCard = NewType('DruidCard', None)
HunterCard = NewType('HunterCard', None)
MageCard = NewType('MageCard', None)
PaladinCard = NewType('PaladinCard', None)
PriestCard = NewType('PriestCard', None)
RogueCard = NewType('RogueCard', None)
ShamanCard = NewType('ShamanCard', None)
WarlockCard = NewType('WarlockCard', None)
WarriorCard = NewType('WarriorCard', None)
NeutralCard = NewType('NeutralCard', None)
AnyHeroCard = Union[DruidCard, HunterCard, MageCard, PaladinCard, PriestCard,
                    RogueCard, ShamanCard, WarlockCard, WarriorCard]


MinionCardType = NewType('MinionCardType', None)
SpellCardType = NewType('SpellCardType', None)
MinionCardValue = NewType('MinionCardValue',
                          Tuple[int, int, List[Effect]]) #Power, Life, [Effect] - Battlecry, Deathrattle ect
SpellCardValue = NewType('SpellCardValue', Tuple[List[Effect], Target])
CardType = NewType('CardType', Tuple[Union[MinionCardType, SpellCardType], AnyHeroCard])
CardValue = NewType('CardValue', Union[MinionCardValue, SpellCardValue])

Card = NewType('Card', Tuple[CardType, CardValue])

Deck = List[Card]
Hand = List[Card]

MinionsOnBoard = Tuple[List[Card], List[Card]] #First player minion, second player minions

Hands = NewType('Hands', Tuple[List[Card], List[Card]])

Heroes = NewType('Heroes', Tuple[Hero, Hero])

Board = NewType('Board', Tuple[MinionsOnBoard])

Decks = NewType('Decks', Tuple[Deck, Deck])

TurnNumber = NewType('TurnNumber', int)

HearthstoneModel = NewType('HearthstoneModel', Tuple[Heroes, Hands, Decks, Board, TurnNumber])

EndTurnMove = NewType('EndTurnMove', None)

Turn = NewType('Turn', List[Union[EndTurnMove]])
