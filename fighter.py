from random import randint

def get_ability(name):
    ability1 = {
        "addison": "RENEGADE",
        "elon": "TUSK BASH",
        "jim": "LECTURE",
        "kanye": "YEEZUS",
        "linus": "NVIDIA LAUNCH",
        "mike": "EAR BITE",
        "niki": "ANACONDA",
        "rick": "RAY GUN",
        "ronaldo": "FAKE INJURY",
        "serena": "SERVE",
        "tiger": "PUT",
        "tom": "RING ATTACK",
        "trump": "FAKE NEWS",
   }
    return ability1.get(name)

def get_ability2(name):
    ability2 = {
        "addison": "FOLLOW ME",
        "elon": "3-2-1 LAUNCH",
        "jim": "HW IS ON BB",
        "kanye": "21 GRAMMYS",
        "linus": "PC BUILD",
        "mike": "LISP",
        "niki": "TOUCH THE SKY",
        "rick": "SLURP",
        "ronaldo": "GOALLLLLL",
        "serena": "SPIKE",
        "tiger": "REHAB",
        "tom": "GOAT'S NEIGH",
        "trump": "YUGE",
   }
    return ability2.get(name)
def use_ability(name):
    # [effect type, effect value]
    #debuff removes all there armor by setting a negative buff to there hero
    #buff increases armor and damage
    #jim, burst, punch and slash deal damage minus armor
    #heal heals TO A MAX OF 100
    #damage is always 1 through 10 times multiplier number.
    effect = {
        "FOLLOW ME": ["debuff",20],
        "3-2-1 LAUNCH": ["burst",6],
        "HW IS ON BB": ["jim",100],
        "21 GRAMMYS": ["slash",5],
        "PC BUILD": ["heal",20],
        "LISP": ["debuff",20],
        "TOUCH THE SKY": ["buff",10],
        "SLURP": ["buff",15],
        "GOALLLLLL": ["slash",7],
        "SPIKE": ["punch",7],
        "REHAB": ["buff",8],
        "GOAT'S NEIGH": ["buff",10],
        "YUGE": ["buff",20],
        "RENEGADE": ["slash",5],
        "TUSK BASH": ["slash",5],
        "LECTURE": ["heal",100],
        "YEEZUS": ["punch",6],
        "NVIDIA LAUNCH": ["burst",5],
        "EAR BITE": ["slash",7],
        "ANACONDA": ["slash",5],
        "RAY GUN": ["burst",7],
        "FAKE INJURY": ["debuff",10],
        "SERVE": ["debuff",10],
        "PUT": ["punch",7],
        "RING ATTACK": ["punch",7],
        "FAKE NEWS": ["slash",5],
   }
    return effect.get(name)
def get_init(name):
    init = {
        "jim": 1,
        "addison": 2,
        "elon": 3,
        "kanye": 4,
        "linus": 5,
        "mike": 6,
        "niki": 7,
        "rick": 8,
        "ronaldo": 9,
        "serena": 10,
        "tiger": 11,
        "tom": 12,
        "trump": 13,
   }
    return init.get(name)

def get_armor(name):
    armor = {
        "jim": 100,
        "addison": 10,
        "elon": 10,
        "kanye": 20,
        "linus": 15,
        "mike": 25,
        "niki": 10,
        "rick": 25,
        "ronaldo": 15,
        "serena": 10,
        "tiger": 5,
        "tom": 20,
        "trump": 10,
   }
    return armor.get(name)

def get_damage(atk_damage):
    damage = atk_damage * randint(0,10)
    return damage
