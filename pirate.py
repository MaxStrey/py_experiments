import random
secret = random.randint(1,99)

guess = 0
tries = 0

print("AHOY! I'm Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99.  I'll give you 6 tries")

while guess != secret and tries < 6:
    user_input = input("What's yer guess?  ")
    guess = int(user_input)

    if guess < secret:
        print("Too low, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")

    tries = tries +1

if guess==secret:
    print("Avast! Ye got it! Found my secret, ye did!")
else:
    print("no more guesses! Better luck next time, matey!")
    print("The secret number was",secret)