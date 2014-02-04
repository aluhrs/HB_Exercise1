import random

print "Hey! What is your name?"
name = raw_input("> ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
number = random.randint(0, 100)
