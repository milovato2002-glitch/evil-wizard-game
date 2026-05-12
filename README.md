# Evil Wizard Battle

A turn-based RPG combat game built in Python using object-oriented programming.

## How to Play

```bash
python wizard_battle.py
```

Choose a character class, name your hero, and battle the Evil Wizard in turn-based combat.

## Character Classes

| Class   | HP  | ATK | Special Abilities              |
|---------|-----|-----|--------------------------------|
| Warrior | 140 | 25  | Power Attack, Shield Wall      |
| Mage    | 100 | 35  | Cast Spell, Magic Barrier      |
| Archer  | 110 | 30  | Quick Shot, Evade              |
| Paladin | 150 | 20  | Holy Strike, Divine Shield     |

## Features

- **4 playable classes** each with unique abilities
- **Heal system** that restores HP without exceeding max
- **Randomized damage** for varied combat encounters
- **Evil Wizard boss** that regenerates health every turn
- **Random wizard attacks** including Fireball, Lightning, and Minion summoning
- **Defensive abilities**: Shield Wall, Evade, and Divine Shield block attacks
- **Turn-based menu system** with clear feedback each round

## OOP Concepts Used

- Inheritance (all classes extend `Character`)
- Encapsulation (health, attack logic within each class)
- Polymorphism (`special_abilities()` method differs per class)

## Requirements

- Python 3.6+
