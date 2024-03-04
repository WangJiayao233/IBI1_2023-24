# What does this piece of code do?
# Answer: Generate a random number between 1 and 10 for 100 times and print out sum of all random numbers.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint
# 
# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
total_random_number=0
while progress<100:
	progress+=1  #count
	n = randint(1,10)   #generate a random number between 1 and 10
	total_random_number = total_random_number+n  # add the random number into the total random number

print(total_random_number)
