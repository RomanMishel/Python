import random

def dice_game():
    dice_num = ""
    user_input = input("To throw a dice type -'start': ")
    dice_1 = """
    +-------+
    |       |
    |   o   |
    |       |
    +-------+
    """

    dice_2 = """
    +-------+
    | o     |
    |       |
    |     o |
    +-------+
    """

    dice_3 = """
    +-------+
    | o     |
    |   o   |
    |     o |
    +-------+
    """

    dice_4 = """
    +-------+
    | o   o |
    |       |
    | o   o |
    +-------+
    """

    dice_5 = """
    +-------+
    | o   o |
    |   o   |
    | o   o |
    +-------+
    """

    dice_6 = """
    +-------+
    | o   o |
    | o   o |
    | o   o |
    +-------+
    """
    if user_input == "start":
        dice_num = random.randint(1,6)
        cpu_try = random.randint(1,6)

        if dice_num > cpu_try:
            if dice_num == 1:
                print("Player wins!")
                print(dice_1)

            elif dice_num == 2:
                print("Player wins!")
                print(dice_2)

            elif dice_num == 3:
                print("Player wins!")
                print(dice_3)

            elif dice_num == 4:
                print("Player wins!")
                print(dice_4)

            elif dice_num == 5:
                print("Player wins!")
                print(dice_5)

            elif dice_num == 6:
                print("Player wins!")
                print(dice_6)

            else:
                print("Error")

        else:
            if cpu_try == 1:
                print("CPU wins!")
                print(dice_1)

            elif cpu_try == 2:
                print("CPU wins!")
                print(dice_2)

            elif cpu_try == 3:
                print("CPU wins!")
                print(dice_3)

            elif cpu_try == 4:
                print("CPU wins!")
                print(dice_4)

            elif cpu_try == 5:
                print("CPU wins!")
                print(dice_5)

            elif cpu_try == 6:
                print("CPU wins!")
                print(dice_6)
            else:
                print("Error")
    else:
        print("Something went wrong!")
        return

dice_game()
