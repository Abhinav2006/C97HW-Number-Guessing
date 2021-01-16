import random
number = random.randint(1,9)
print("Guess a number between 1 to 9")
count = 5
while count > 0:
    guess = int(input("Your guess:"))
    if guess < number:
        print("Number is greater than your guess")
    elif guess > number:
        print("Number is less than your guess")
    else:
        print("Congratulations you win!")
        break
    count = count - 1
if count == 0:
    print("You have run out of chances, You Lose")