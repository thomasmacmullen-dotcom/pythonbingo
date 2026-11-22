Python Bingo
Version: Beta 0.6 (documentation draft)

Python Bingo is a terminal-based Bingo project written in Python. It includes a randomized Bingo number caller and a generator for traditional 5 × 5 Bingo cards. The project is developed incrementally to demonstrate foundational Python programming concepts and how software evolves from one beta release to the next.
Documentation note: The Beta 0.6 source code has not yet been provided for review. Features below are confirmed from Beta 0.5; any Beta 0.6 changes still need verification before this README is published as a final release description.

Confirmed features
- Number caller: Randomly selects from the standard set of 75 Bingo numbers, with the corresponding B, I, N, G, or O prefix.
- No duplicate calls within a session: Removes numbers from the available pool after they are called.
- Session history: Displays the list of numbers called when the caller ends the session.
- Card generator: Creates randomized 5 × 5 cards with traditional Bingo column ranges.
- Free center square: Displays FREE in the center of the card.
- Terminal interface: Uses a text-based menu to select caller or card-generator mode.
Requirements
- Python 3
- No third-party dependencies for the confirmed features (random is part of the Python standard library).
Running the program
Save bingo.py in a folder, open a terminal in that folder, and run:
python bingo.py
On systems using python3 as the command, run:
python3 bingo.py
How to use
Calling numbers
Select 1 from the main menu to call numbers. Each call produces a letter-number combination such as B7 or O64. When asked Called Bingo (y/n), enter n to continue or y to stop and display the called-number list.
Creating a card
Select 2 from the main menu to generate a random Bingo card. The columns use these ranges:
Column	Numbers
B	1–15
I	16–30
N	31–45
G	46–60
O	61–75


The center square is FREE.

Version history
Version	Notes
Beta 0.5	Initial documented number-caller and card-generator functionality
Beta 0.6:
# 1. Moved printing Bingo card to its own function
# 2. Added gametype as dictionary
# 3. Added choice of game option
# 4. Added main() function

Proposed Future Features:

- Validating every menu and game input
- Saving number calls across sessions
- Marking called numbers on the displayed card
- Detecting completed winning patterns
- Handling exhaustion of all 75 numbers in caller mode


Python concepts
The confirmed implementation demonstrates functions, lists, list comprehensions, loops, conditionals, random selection, formatted string output, and console input. Later versions may add more concepts as the project develops.
Project status
Beta / work in progress. This document is a provisional README for Beta 0.6, not a verified feature inventory of that release.
