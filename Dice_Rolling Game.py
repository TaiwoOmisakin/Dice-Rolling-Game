import random

while True:
    choice= input("Roll the dice? (y/n): ").upper
    if choice == "Y":
        no1= random.randint(1,6)
        no2= random.randint(1,6)
        print(f"({no1}, {no2})")
    elif choice== "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")

