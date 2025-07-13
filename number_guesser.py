import random
a = int(input("Upper limit? "))
b = int(input("Lower limit? "))
ga = int(input("Amount of guesses? "))
n = random.randint(b,a)
for i in range(ga):
    guess = int(input("Guess a number: "))
    if guess < n:
        print("Go higher!")
    elif guess > n:
        print("Go lower!")
    else:
        print("Correct!")
        break
else:
    print("Out of attempts!")
    print("The number was", n)