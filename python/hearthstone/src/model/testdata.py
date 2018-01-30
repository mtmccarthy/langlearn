from src.model.Types import *

#Effects
DestroyOpponentWeaponEffect = Effect
GiveMinionHealthEffect = Effect
GiveMinionTauntEffect = Effect
SummonRandomBeastEffect = Effect
DealDamageToEnemyEffect = Effect
DrawCardEffect = Effect
IncreaseSpellDamageEffect = Effect
DestroyEnemyMinionEffect = Effect
GiveMinionPowerEffect = Effect
GainArmorEffect = Effect


#Cards
AcidicSwampOoze = Card(((MinionCardType, NeutralCard),
                        MinionCardValue((3, 2, [DestroyOpponentWeaponEffect]))))

AncestralHealing = Card(((SpellCardType, ShamanCard),
                         SpellCardValue(
                             ([GiveMinionHealthEffect, GiveMinionTauntEffect], Target)
                         )))

druidSampleDeck = [AcidicSwampOoze] * 15 + [AncestralHealing] * 15

paladinSampleDeck = [AcidicSwampOoze] * 15 + [AncestralHealing] * 15