#Brandon Nichols
#Prof 'Jay' 'Gaines' Cis 261
#Guessing Game
import random
Name = input(" Enter Your Name\n")

def Title():
    print("Welcome to the guessing game")
    print()

def Game_Play(limit):
    number = random.randint(1, limit)
    print(f" im thinking of a number of 1 and {limit}\n")
    count = 1
    guess = int(input("your guess?:    "))
    while (guess != number):
        if guess < number:
            print("To Low")
            count +=1
        elif guess > number:
            print("To High")
            count +=1
        guess = int(input("your guess?:   "))
    print(f"You finished in {count} tries Good Job Stranger {Name}")
def main():
    Title()
    again = "yes"
    while again.lower() == "yes":
        limit =(int(input(f"Enter the limit:")))
        Game_Play(limit)
__name__ == "__main__"
main()






    