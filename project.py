import random
print("no guessing game")

no=random.randint(1,9)
chance=0
print("Guess a no between 1 to 9")
while chance<5:
    guess=int(input("enter the guess"))
    if guess== no:
        print ("congo you won")
        break
    elif guess<no:
        print("Your guess was too low guess a higher no than",guess)
    else:
        print("your guess was too high guess a lower no than",guess)
    chance=chance+1
if not chance<5:
    print("You lose the no is",no)