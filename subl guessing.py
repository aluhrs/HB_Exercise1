import random


print "Hey! What is your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
number = random.randint(1, 100)

i = 1

while True:

    print "Your guess?"
    guess = raw_input("> ")
    

    if not guess.isdigit():
        print "That's not an int! Try again!"
    elif int(guess) > number:
        print "Your guess is too high: try again."
    elif int(guess) < number:
        print "Your guess is too low: try again."
    else:
        if i == 1:
            print "Well done, %s! You found my number in your first try!" % (name)
        else:
            print "Well done, %s! You found my number in %i tries!" % (name, i)
        break

    i += 1