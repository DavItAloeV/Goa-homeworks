import random

import random

your_points = 0
computer_points = 0
round = int(input("How many round do you want?: "))

while computer_points < round and your_points < round:

    choice = input("please enter a choice(rock/paper/scissors) ")
    if choice == "rock":
        print("you chose rock")
    elif choice == "paper":
        print("you chose paper")
    elif choice == "scissors":
        print("you chose scissors")
    else:
        print("invalid choice")
    #აქ წერია ამაში ანუ ინ ამით აქედან რამე თუ არ იყო დაწერს რა არჩეული ქონდა და რომ რაღაცა სხვა თუ დაწერე ამოაგდებს რომ არ არის ეგეთი არჩევანი

    if choice in ["rock", "paper", "scissors"]:
        computer = random.choice(["rock", "paper", "scissors"])
        print("computer chose:", computer) 

    if choice== "rock" and  computer == "paper":
        print("computer won")
        computer_points += 1
        print("Your points : ", your_points, " Computer points : ", computer_points) 
    if choice== "paper" and computer =="scissors":
        print("computer won")
        computer_points += 1
        print("Your points : ", your_points, " Computer points : ", computer_points)  
    if choice=="scissors" and computer == "rock":
        print("computer won")
        computer_points += 1
        print("Your points : ", your_points, " Computer points : ", computer_points)  
    if choice=="rock" and computer == "scissors":  
        print("you won")
        your_points += 1
        print("Your points : ", your_points, " Computer points : ", computer_points) 
    if choice=="scissors" and computer == "paper": 
        print("you won")
        your_points += 1
        print("Your points : ", your_points, " Computer points : ", computer_points) 
    if choice=="paper" and computer == "rock":
        print("you won")
        your_points += 1
        print("Your points : ", your_points, " Computer points : ", computer_points) 
    if choice=="paper" and computer == "paper":
        print("draw")
        print("Your points : ", your_points, " Computer points : ", computer_points)      
    if choice=="scissors" and computer == "scissors":
        print("draw")
        print("Your points : ", your_points, " Computer points : ", computer_points) 
    if choice=="rock" and computer == "rock":
        print("draw") 
        print("Your points : ", your_points, " Computer points : ", computer_points)
    if choice=="scissors" and computer=="rock":      
        print("computer won")
        print("Your points : ", your_points, " Computer points : ", computer_points)
    if choice=="scissors" and computer=="paper":
        print("you won")


choice = input("Enter a value: ")

try:
    num = int(choice)
    
    if num < 0:
        print(f"You entered a negative number: {abs(num)}")  
    else:
        print("Invalid choice") 
except ValueError:
    print("Invalid choice")



