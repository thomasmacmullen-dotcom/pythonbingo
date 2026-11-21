import random


def gametype():
    gametype = ['Vertical', 'Horizontal', 'Diagonal', 'Full Card']


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

    # Print the Bingo card
    print("=================================")
    print("  B     I     N     G     O")
    print("=================================")

    for row in range(5):
        print(f"{str(B[row]):^6}{str(I[row]):^6}"
              f"{str(N[row]):^6}{str(G[row]):^6}"
              f"{str(O[row]):^6}")

    print("=================================")


if showmenu() == 1:
    callnumber()
else:
    create_card()