############# Python Bingo ######################
# Beta Version .6
# Changes:
# 1. Moved printing Bingo card to its own function
# 2. Added gametype as dictionary
# 3. Added choice of game option
# 4. Added main() function


import random

def printcard(B, I, N, G, O):
    # Print the Bingo card
    print("=================================")
    print("  B     I     N     G     O")
    print("=================================")

    for row in range(5):
        print(f"{str(B[row]):^6}{str(I[row]):^6}"
              f"{str(N[row]):^6}{str(G[row]):^6}"
              f"{str(O[row]):^6}")

    print("=================================")

def gametype():
    gametype = {
        "Vertical": 1,
        "Horizontal": 2,
        "Diagonal": 3,
        "Full Card": 4
    }

    print("Choose a Bingo Game Type:")

    for game, number in gametype.items():
        print(f"{number}. {game}")

    # Get the user's choice
    while True:
        choice = int(input("Enter your choice (1-4): "))

        # Find the selected game
        for game, number in gametype.items():
            if choice == number:
                print(f"You selected {game}")
                return choice
        else:
            print("Invalid selection!")


def showmenu():
    print("=================================")
    print("======= Welcome to Bingo! =======")
    print("Choose 1 to call numbers")
    print("Choose 2 to create card")
    mychoice = int(input("Choose your choice: "))
    return mychoice


def get_bingo_numbers():
    bingonumbers = [f"B{n}" for n in range(1, 16)] + \
                   [f"I{n}" for n in range(16, 31)] + \
                   [f"N{n}" for n in range(31, 46)] + \
                   [f"G{n}" for n in range(46, 61)] + \
                   [f"O{n}" for n in range(61, 76)]
    return bingonumbers


def callnumber():
    callednumbers = []
    bingonumbers = get_bingo_numbers()
    while True:
        number = random.choice(bingonumbers)
        callednumbers.append(number)
        print(number)
        bingonumbers.remove(number)
        bingodone = input("Called Bingo (y/n)").lower()
        if bingodone == 'y':
            print(callednumbers)
            break


def create_card():
    # Generate five columns of random numbers
    B = random.sample(range(1, 16), 5)
    I = random.sample(range(16, 31), 5)
    N = random.sample(range(31, 46), 5)
    G = random.sample(range(46, 61), 5)
    O = random.sample(range(61, 76), 5)

    # The center square is always FREE
    # We overwrite N[2] which was actually assigned a number
    # Possibly correct that behavior if needed
    N[2] = "FREE"

    printcard(B, I, N, G, O)
    return B, I, N, G, O

def main():
    if showmenu() == 1:
        callnumber()
    else:
        mygametype = gametype()
        B, I, N, G, O = create_card()
        bingocard = [B, I, N, G, O]
        numbercalled = int(input("Enter the number called: "))


if __name__ == "__main__":
    main()

