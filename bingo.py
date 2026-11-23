############# Python Bingo ######################
# Beta Version .7
# Changes:
# 1. Added error checking to showmenu and gametype
# 2. Added file to keep track of called numbers
# 3. After a number is entered, card redraws
# 4. Added checkbingo function


import random

def checkbingo(B, I, N, G, O, numbercalled):

    numbercalled = numbercalled.upper().strip()

    columns = {
        "B": B,
        "I": I,
        "N": N,
        "G": G,
        "O": O
    }

    if len(numbercalled) < 2:
        print("Invalid number!")
        return False

    letter = numbercalled[0]

    try:
        number = int(numbercalled[1:])
    except ValueError:
        print("Invalid number!")
        return False

    if letter not in columns:
        print("Invalid Bingo letter!")
        return False

    if number in columns[letter]:
        print("Number found!")
        return True
    else:
        print("Number not found!")
        return False


def openfile():
        with open('callednumbers.txt', 'w') as file:
            return file

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
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                break
            except ValueError:
                print("Please enter a number.")

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
    while True:
        try:
            mychoice = int(input("Choose your choice: "))
            if mychoice < 1 or mychoice > 2:
                print("Please enter a number between 1 and 2.")
            else:
                return mychoice
        except ValueError:
            print("Please enter a number between 1 and 2.")



def get_bingo_numbers():
    bingonumbers = [f"B{n}" for n in range(1, 16)] + \
                   [f"I{n}" for n in range(16, 31)] + \
                   [f"N{n}" for n in range(31, 46)] + \
                   [f"G{n}" for n in range(46, 61)] + \
                   [f"O{n}" for n in range(61, 76)]
    return bingonumbers


def callnumber():
    try:
        with open('callednumbers.txt', 'a') as file:

            callednumbers = []
            bingonumbers = get_bingo_numbers()
            while True:
                number = random.choice(bingonumbers)
                callednumbers.append(number)
                file.write(f"{number}\n")
                print(number)
                bingonumbers.remove(number)
                bingodone = input("Called Bingo (y/n)").lower()
                if bingodone == 'y':
                    print(callednumbers)
                    break
    except FileNotFoundError:
        openfile()

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
        numbercalled = "0"
        mygametype = gametype()
        B, I, N, G, O = create_card()
        bingocard = [B, I, N, G, O]
        while numbercalled != "BINGO":
            numbercalled = input("Enter the number called: ")
            print(numbercalled)
            isoncard = checkbingo(B,I,N,G,O, numbercalled)
            printcard(B, I, N, G, O)

if __name__ == "__main__":
    main()
