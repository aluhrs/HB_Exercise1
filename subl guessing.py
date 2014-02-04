import random

print "Hey! What is your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
number = random.randint(0, 100)

print "Your guess?"
guess = int(raw_input("> "))

while True:
    if guess > number:
        print "Your guess is too high: try again."
        num_guesses.append(i)
        print "Your guess?"
        guess = int(raw_input("> "))
    elif guess < number:
        print "Your guess is too low: try again."
        print "Your guess?"
        guess = int(raw_input("> "))
    else:
        print "Well done, %s! You found my number in %i tries!" % name
        break