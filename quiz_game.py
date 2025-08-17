def play_quiz():
    print("Welcome to my quiz game")

    playing = input("Do you want to play a quize game? ")

    if playing.lower() != "yes":
        quit()

        

    print("Lets play a game")
    score = 0

    answer = input("What is the full form of CPU? ").strip()
    if answer.lower() == "central processing unit":
        print("Correct")
        score += 1
 
    else:
        print("Incorrect!")

    answer = input("What is the full form of GPU? ").strip()
    if answer.lower() == "graphics processing unit":
        print("Correct")
        score += 1 
    else:
        print("Incorrect!")

    answer = input("What is the full form of RAM? ").strip()
    if answer.lower() == "Random Access Memory":
        print("Correct")
        score += 1

 
    else:
        print("Incorrect!")
#final score
    print("you got " + str(score) + " " + "questions correct!")
    print("you got " + str((score / 3) * 100) + " " + "%.")
#feedback
    if score == 3:
        print("Excellent")
    if score == 2:
        print("Good Job")
    if score == 1:
        print("Keep Practicing")
# Replay option
    again = input("Do you want to play again? (yes/no)").lower()
    if again == "yes":
        play_quiz()
    else:
        print("thank you for playing")

play_quiz()








