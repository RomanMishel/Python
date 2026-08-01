import random

def RPS():
    Rock = "1"
    Paper = "2" 
    Scissors = "3"
        
    player_1_choice = input("Player 1 choose your move: ")
    cpu_choice = random.choice([Rock, Paper, Scissors])

    if player_1_choice == cpu_choice :
        print("Draw, Try again!")
        return

    elif player_1_choice == Scissors and cpu_choice == Paper:
        print("Scissors beat Paper, Player 1 wins")
        return
    
    elif player_1_choice == Rock and cpu_choice == Scissors:
        print("Rock beats Scissors, Player 1 wins")
        return
    
    elif player_1_choice == Paper and cpu_choice == Rock:
        print("Paper beats Rock, Player 1 wins")
        return
    
    else: 
        print("CPU wins")
        return
RPS()