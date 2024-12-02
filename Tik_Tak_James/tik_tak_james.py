# players
players = [1, 2]
user = "X"
bot = "O"
symbol = ""

# tableau
board = [["_", "_", "_"], ["_", "_", "_"], [" ", " ", " "]]
line1 = board[0]
line2 = board[1]
line3 = board[2]

# switch players between rounds
def switch_player():
    global tour
    while tour < 6:
        print("Tour numéro : ", tour)
        for player in players:
            if player == 1:
                global symbol
                symbol = user
                print("Player 1, your move: ")
            else:
                symbol = bot
                print("Player 2, your move: ")
            moves()
        tour += 1
    
# moves
def moves():
    play1 = int(input("On which line do you wish to play ? (1,2,3) : "))
    play2 = int(input("Which section you wish to put your symbol ? (1,2,3) : "))
    # error if number isnt 1,2 or 3
    if play1 != 1 and play1 != 2 and play1 != 3:
        print("1- Error, Enter a number 1, 2 or 3")
        return play1
    elif play2 != 1 and play2 != 2 and play2 != 3:
        print("2- Error, Enter a number 1, 2 or 3")
        return play2
    else: 
        # line 1
        if play1 == 1:
            line1[play2 - 1] = symbol
        # line 2
        elif play1 == 2:
            line2[play2 - 1] = symbol
        # line 3
        elif play1 == 3:
            line3[play2 - 1] = symbol
        print("|".join(line1))
        print("|".join(line2))
        print("|".join(line3))
    
# starting the game
def game():
    print("Welcome to Tik Tak Toe ! ")
    start = input("Do you want to play ? [Y]es/[N]o ")
    if start.lower() != "y" and start.lower() != "yes" and start.lower() != "n" and start.lower() != "no":
        print("Error! Enter [Y]es or [N]o ")
        return game()
    elif start.lower() == "n" or start.lower() == "no":
        print("Bye !")
    elif start.lower() == "y" or start.lower() == "yes":
        print("|".join(line1))
        print("|".join(line2))
        print("|".join(line3))
        switch_player()

game()