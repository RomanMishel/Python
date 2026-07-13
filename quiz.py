from random import choice

def quiz():
    
    question_1 = "What is the capital of Great Britane?"
    question_2 = "What is the capital of France?"
    question_3 = "What is the capital of Russia?"
    
    random_question = choice([question_1, question_2, question_3])
    print(random_question)
    score = 0
    answer = input("Enter your answer: ")

    if random_question == question_1 and answer == "London":
        print("Correct answer!")
        score += 1
        print(f"Your score is {score}")
    elif random_question == question_2 and answer == "Paris":
        print("Correct answer!")
        score +=1
        print(f"Your score is {score}")
    elif random_question == question_3 and answer == "Moscow":
        print("Correct answer!")
        score +=1
        print(f"Your score is {score}")
    else:
        print("Incorrect answer")

quiz()
