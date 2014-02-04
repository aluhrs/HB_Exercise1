import random


print "Hey! What is your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
number = random.randint(1, 101)

print "Your guess?"
guess = int(raw_input("> "))

i = 1

while True:
    if guess > number:
        print "Your guess is too high: try again."

    elif guess < number:
        print "Your guess is too low: try again."
        
    else:
        print "Well done, %s! You found my number in %i tries!" % (name, i)
        break

    i = i + 1
    print "Your guess?"
    guess = int(raw_input("> "))