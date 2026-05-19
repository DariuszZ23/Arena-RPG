# 🏟️ Arena RPG

A simple text-based RPG game written in Python using Object-Oriented Programming (OOP).
The player controls a knight fighting against a goblin controlled by a simple AI system.
---
## 📖 Project Description

This project presents a basic turn-based combat system where:

the player chooses an action every turn,
the enemy performs actions automatically,
characters have stats and abilities,
attacks include a random damage factor.

The code demonstrates:

abstract classes (ABC),
inheritance,
polymorphism,
combat system encapsulation.
---
# ⚔️ Game Mechanics
## 👤 Player — Knight
```
Statistic	Value
HP	90
Attack	20
Defense	5
Abilities:
Attack — deals damage to the enemy
Heal — restores 10 HP
```
## 👾 Enemy — Goblin
```
Statistic	Value
HP	80
Attack	37
Defense	2
```
## AI Behavior:
attacks automatically,
uses healing only once,
heals itself when HP drops below 30%.
---
## 🧩 Damage System

Damage is calculated using the following formula:

damage=max(0, attack−defense+random(−2,5))

This adds a small random factor to each attack, making combat less predictable.
---
## 🏗️ Project Architecture
# Main Classes
## Game

Responsible for starting the game and initializing the battle system.

## BaseCharacter

Abstract base class for all characters.

Contains:

* HP,
* attack,
* defense,
* damage and healing logic.
## Player

Class controlled by the user.

Features:

* action selection,
* character status display.
## Enemy

Enemy controlled by simple AI logic.

## Ability

Abstract base class for abilities.

## Attack

Implements the damage-dealing ability.

## Heal

Implements healing functionality.

## BattleSystem

Handles:

* battle flow,
* turn order,
* win/lose conditions.
## 📂 Project Structure
```
arena-rpg/
│
├── main.py
└── README.md
```
---
## 🚀 Running the Project
Requirements
* Python 3.x
---
## Start the Game
```bash
python main.py
```
---
## 🎮 Example Gameplay
```
=== Arena RPG ===

Your turn:
Knight HP: 90/90
Goblin HP: 80/80

1. Attack
2. Heal

Choose action: 1

Knight deals 21 damage!
Goblin deals 34 damage!
```
---
## 🧠 Programming Concepts Used

This project demonstrates:

* Object-Oriented Programming (OOP)
* Inheritance
* Polymorphism
* Abstract Classes (ABC)
* Encapsulation
* Separation of responsibilities
---
## Author
Dariusz Zerynger
---