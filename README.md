Python Bingo

A Python Programming Teaching Aid

Python Bingo is a terminal-based Bingo application developed as a teaching aid for students enrolled in introductory Python programming courses.

The project demonstrates fundamental programming concepts through a familiar, interactive game. Students can explore how functions, lists, dictionaries, loops, conditional statements, random number generation, exception handling, and file operations work together in a practical application.

Rather than presenting a finished application, Python Bingo is being developed and published incrementally. Each beta release introduces new functionality, improves existing code, or addresses limitations identified in earlier versions.

This approach allows students to observe the software development process, including debugging, testing, code organization, and iterative improvement.

Educational Objectives

The project is intended to help introductory programming students:

Understand how individual programming concepts work together in a complete application.

Practice working with lists and dictionaries to organize and manipulate data.

Explore functions and modular program design.

Apply loops, conditional statements, and input validation.

Understand random number generation and preventing duplicate selections.

Examine file handling and data persistence.

Recognize the importance of testing, debugging, and incremental software development.

Development Philosophy

One of the central lessons of introductory programming is that a working application does not have to be complicated from the beginning.

Python Bingo began with basic number calling and Bingo card generation. Subsequent versions build on that foundation, introducing additional capabilities while providing opportunities to revisit and improve earlier code.

By preserving the beta releases, students can compare versions, identify changes, and see how a simple program evolves over time.

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
Beta 0.7:
# 1. Added error checking to showmenu and gametype
# 2. Added file to keep track of called numbers
# 3. After a number is entered, card redraws
# 4. Added checkbingo functio

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
