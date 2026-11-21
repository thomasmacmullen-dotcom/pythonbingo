Python Bingo
Current version: Beta 0.5

Python Bingo is a simple, terminal-based Bingo program written in Python. It can serve as a Bingo number caller or generate a randomized Bingo card for a player. This is a work in progress, developed incrementally to explore practical Python programming concepts.
Features in Beta 0.5
- Two modes: choose to call Bingo numbers or create a Bingo card.
- Random number calling: draws from the standard 75-number Bingo pool, with the appropriate B, I, N, G, or O prefix.
- No repeated calls in a session: each called number is removed from the remaining pool.
- Called-number history: when the caller indicates that Bingo has been called, the program prints the numbers drawn during that session.
- Random card generation: creates a text-based 5 × 5 Bingo card using the traditional number ranges for each column.
- Free center square: the middle square is marked FREE.
Requirements
- Python 3
- No third-party packages. The program uses Python's built-in random module.

Getting started
1. Download or clone this repository.
2. Open a terminal in the folder containing bingo.py.
3. Run:
   python bingo.py
   On systems where Python 3 is invoked as python3, use python3 bingo.py instead.
How to use
When the program starts, it displays this menu:
=================================
======= Welcome to Bingo! =======
Choose 1 to call numbers
Choose 2 to create card
Choose your choice:
Option 1: Call numbers
Enter 1 to start calling numbers. The program selects and prints one number at a time, such as B7 or O64, and asks:
Called Bingo (y/n)
- Enter n to draw another number.
- Enter y to end the session and display the list of called numbers.
Option 2: Create a card
Enter 2 to generate and display one random Bingo card. Numbers follow the standard column ranges:
Column	Range
B	1–15
I	16–30
N	31–45
G	46–60
O	61–75


The center square is FREE. In Beta 0.5, card mode displays a card and then exits; it does not yet accept called numbers or check for a win.
Current limitations
Beta 0.5 is an early prototype:
- The program does not validate menu input, so nonnumeric input can cause an error.
- Generated cards are displayed but are not saved or marked as numbers are called.
- Automatic winning-pattern detection is not implemented.
- Called numbers are held in memory for the current session, not saved to a file.
- The gametype() function contains a list of possible game types (vertical, horizontal, diagonal, full card), but game-type selection is not yet connected to gameplay.
- The number caller does not handle exhausting all 75 numbers before a Bingo is declared.
Version history
Version	Status	Notes
Beta 0.5	Current	Basic number-calling mode and randomized Bingo-card generation.

Python concepts demonstrated
This project uses functions, lists, loops, conditionals, user input, formatted strings, list comprehensions, and random selection with random.choice() and random.sample().
Project status
Beta / work in progress. This README describes the uploaded Beta 0.5 implementation only. Later versions will be documented as they are added to the repository.
