🏟️ Arena RPG (Python CLI)

Prosta gra RPG w trybie tekstowym napisana w Pythonie, oparta na systemie walki turowej. Gracz kontroluje postać rycerza i walczy przeciwko przeciwnikowi sterowanemu przez AI.

📖 Opis

Arena RPG to konsolowa gra, w której gracz podejmuje decyzje w każdej turze walki. System wykorzystuje programowanie obiektowe (OOP) oraz klasy abstrakcyjne do definiowania postaci i umiejętności.

Projekt demonstruje:

dziedziczenie i abstrakcję (ABC)
system umiejętności (abilities)
prostą sztuczną inteligencję przeciwnika
losowość w obrażeniach
⚔️ Mechanika gry
🧙 Postacie
Gracz (Player)
Klasa: Knight
HP: 90
Atak: 20
Obrona: 5
Umiejętności:
Attack – zadaje obrażenia
Heal – leczy 10 HP
Przeciwnik (Enemy)
Klasa: Goblin
HP: 80
Atak: 37
Obrona: 2
AI:
Używa leczenia tylko raz
Leczy się, gdy HP spadnie poniżej 30%
🧩 System walki
Walka odbywa się w turach:
Gracz wybiera akcję
Przeciwnik wykonuje ruch automatycznie
Obrażenia są obliczane jako:
damage = attack - defense + losowość (-2 do +5)
HP nigdy nie spada poniżej 0
Leczenie nie przekracza maksymalnego HP
🧠 Architektura

Projekt oparty jest o podejście obiektowe:

Kluczowe klasy:
Game – uruchamia grę
BattleSystem – zarządza walką
BaseCharacter (abstract)
wspólne cechy postaci
Player – sterowany przez użytkownika
Enemy – prosty AI
Ability (abstract)
Attack
Heal
📂 Struktura projektu
arena-rpg/
│
├── main.py   # cały kod gry
└── README.md
🚀 Uruchomienie
Wymagania
Python 3.x
Start gry
python main.py
🎮 Jak grać
Uruchom grę
W swojej turze wybierz akcję:
1 – Attack
2 – Heal
Pokonaj przeciwnika zanim on pokona Ciebie
🤖 AI przeciwnika

Goblin:

atakuje w każdej turze
używa leczenia tylko raz
robi to automatycznie przy niskim HP
🔮 Możliwe rozszerzenia

Projekt jest dobrą bazą do rozwoju. Możesz dodać:

🧙 więcej klas postaci (Mage, Archer)
🎒 system ekwipunku
📈 levelowanie i doświadczenie
👥 wielu przeciwników
💥 nowe umiejętności (np. krytyki, buffy)
🌐 wersję webową (np. Flask / FastAPI)