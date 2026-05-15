# 🏟️ Arena RPG

Prosta tekstowa gra RPG napisana w Pythonie z wykorzystaniem programowania obiektowego (OOP).
Gracz wciela się w rycerza walczącego na arenie przeciwko goblinowi sterowanemu przez prostą sztuczną inteligencję.
---
## 📖 Opis projektu

Projekt przedstawia prosty system walki turowej, w którym:

* gracz wybiera akcję w każdej turze,
* przeciwnik wykonuje ruch automatycznie,
* postacie posiadają statystyki i umiejętności,
* obrażenia zawierają element losowości.

Kod wykorzystuje:

* klasy abstrakcyjne (ABC),
* dziedziczenie,
* polimorfizm,
* enkapsulację logiki walki.
---
# ⚔️ Mechanika gry
## 👤 Gracz — Knight
```
Statystyka	Wartość
HP      	90
Attack	        20
Defense	        5
```
---
# Umiejętności:
* Attack — zadaje obrażenia przeciwnikowi
* Heal — odnawia 10 HP
## 👾 Przeciwnik — Goblin
```
Statystyka	Wartość
HP      	80
Attack	        37
Defense	        2
```
---
## Zachowanie AI:
* przeciwnik atakuje automatycznie,
* używa leczenia tylko raz,
* leczy się przy HP poniżej 30%.
---
## 🧩 System obrażeń

Obrażenia obliczane są według wzoru:

damage=max(0, attack−defense+random(−2,5))

Dzięki temu każda walka posiada element losowości.
---
---
🏗️ Architektura projektu
Główne klasy
Game

Odpowiada za uruchomienie gry i inicjalizację systemu walki.

BaseCharacter

Abstrakcyjna klasa bazowa dla wszystkich postaci.

Zawiera:

HP,
attack,
defense,
system obrażeń i leczenia.
Player

Klasa sterowana przez użytkownika.

Funkcje:

wybór akcji,
wyświetlanie statusu postaci.
Enemy

Przeciwnik sterowany przez prostą AI.

Ability

Abstrakcyjna klasa bazowa dla umiejętności.

Attack

Implementuje zadawanie obrażeń.

Heal

Implementuje leczenie postaci.

BattleSystem

Obsługuje:

przebieg walki,
kolejność tur,
sprawdzanie zwycięzcy.
---
📂 Struktura projektu
```
arena-rpg/
│
├── main.py
└── README.md
```
---
🚀 Uruchomienie projektu
Wymagania
Python 3.x
---
Start gry
python main.py
---
🎮 Przykładowa rozgrywka
=== Arena RPG ===

Your turn:
Knight HP: 90/90
Goblin HP: 80/80

1. Attack
2. Heal

Choose action: 1

Knight deals 21 damage!
Goblin deals 34 damage!
---
🧠 Zastosowane koncepty programistyczne

Projekt wykorzystuje:

Programowanie obiektowe (OOP)
Dziedziczenie
Polimorfizm
Klasy abstrakcyjne (ABC)
Enkapsulację
Podział odpowiedzialności klas
---