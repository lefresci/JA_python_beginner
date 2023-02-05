import random


def quantity_input():
    print("How many pencils would you like to use:")
    while True:
        quantity = input()
        if not quantity.isdigit():
            print("The number of pencils should be numeric")
            continue
        if quantity == "0":
            print("The number of pencils should be positive")
            continue
        return int(quantity)


def name_input():
    player = input("Who will the first (John, Jack):\n")
    while (player != "Jack") and (player != "John"):
        print("Choose between 'John' and 'Jack'")
        player = input()
        continue
    return player


def index_changing(x):
    if x == 0:
        x = 1
    else:
        x = 0
    return x


def turn_input():
    while True:
        turn = input()
        if turn not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            continue
        return int(turn)


def bot(x):
    """Return the integer for the best turn in pencil game \n
    :param x: current quantity
    :return: sticks quantity that is necessary to save the winning position or just at random if the losing position
    """
    if x == 1:
        return 1
    elif (x - 1) % 4 == 0:
        return random.randint(1, 3)
    else:
        return (x - 1) % 4


def pencil_case():
    quantity = quantity_input()
    player = [name_input()]
    if "John" in player:
        player.append("Jack")
    else:
        player.append("John")
    index = 0
    turn_saver = True
    while quantity > 0:

        if turn_saver:
            print("|" * quantity)
            print(player[index] + "'s turn:")
        turn_saver = True

        if player[index] == "John":
            turn = turn_input()
        else:
            turn = bot(quantity)
            print(turn)

        if quantity < turn:
            print("Too many pencils were taken")
            turn_saver = False
            continue

        quantity -= turn
        index = index_changing(index)

    print(player[index], "won!")


pencil_case()
