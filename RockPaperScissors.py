def RPS():
    Rock = "1"
    Paper = "2" 
    Scissors = "3"
        
    player_1_choice = input("Player 1 choose your move: ")
    player_2_choice = input("Player 2 choose your move: ")

    if player_1_choice == player_2_choice :
        print("Draw ,Try again")
        return

    elif player_1_choice == Rock and player_2_choice == Paper:
        print("Rock beats Paper, Player 1 wins")
        return
    elif player_1_choice == Scissors and player_2_choice == Paper:
        print("Scissors beat Paper, Player 1 wins")
        return
    elif player_1_choice == Rock and player_2_choice == Scissors:
        print("Rock beats Scissors, Player 1 wins")
        return
    else: 
        print("Player 2 wins")
        return
RPS()



    

