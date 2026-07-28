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

        if dice_game > cpu_try:
            