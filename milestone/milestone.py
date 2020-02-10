
def printMap(list):
    print("      |      |      ")
    print(f"   {list[0]}  |   {list[1]}  |   {list[2]}   ")
    print("      |      |      ")
    print("------ ------ ------")
    print("      |      |      ")
    print(f"   {list[3]}  |   {list[4]}  |   {list[5]}   ")
    print("      |      |      ")
    print("------ ------ ------")
    print("      |      |      ")
    print(f"   {list[6]}  |   {list[7]}  |   {list[8]}   ")
    print("      |      |      ")


printMap(["x", "x", "x", "0", "0", "0", "0", "0", "x"])


def startGame():
    player1 = ''
    player2 = ''
    print("Hello and welcome to the tick tack toe game")
    print("Author Eduardo Avila")
    print("First things firts")
    while True:
        player1 = input(
            "Player one select your simbol X or O chose wisely ").upper()
        if player1.upper() != "X" and player1.upper() != "O":
            print("Invalid input chose one of these X or O")
        else:
            break
    player2 = "O" if player1.upper() == "X" else "X"

    print(f"Ok then the player1 is {player1} ")
    print(f"And then the player2 is {player2} ")


startGame()
