import random
computer = 0
you = 0
tie = 0
l = ["rock", "paper","scissors"]
g=1
i=1

while True:
    print("\n\nROUND",i,"BEGINS")
    choice = random.choice(l)
    string = input("\nEnter your choice [rock,paper,scissors] \"Enter key to stop\":")
    string = string.lower()
    if string==choice:
        print("IT IS A TIE")
        tie+=1
        i+=1
        
    elif (string == "rock" and choice == "scissors") or (string == "paper" and choice == "rock") or (string == "scissors" and choice == "paper"):
        print("YOU WON")
        print("Computer's choice was",choice)
        you+=1        
        i+=1
        
    elif (string == "scissors" and choice == "rock") or (string == "rock" and choice == "paper") or (string == "paper" and choice == "scissors"):
        print("YOU LOST")
        print("Computer's choice was",choice)
        computer+=1       
        i+=1
    elif string == "":
        break
        
    else:
        print("Invalid input Try again")
    
        
    
    
       
print("\n\nYOU WON IN",you,"ROUNDS")
print("THE COMPUTER WON IN",computer,"ROUNDS")
print(tie,"ROUNDS TIE")
