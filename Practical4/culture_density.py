p = 5
i = 0
# p is 5 firstly.
# Repeat:  p doubles
# How many times completed?
#            If p is less than 90: p doubles again 
#            If p is more than 90: DONE
#To count the times, set a variable i to show the maximum day
#When printing, use str(i) to make the result i into a string, which can be printed out in a long string.

while (p <= 90):
    i += 1
    p = p * 2

print("On day "+str(i)+ " the cell density goes over 90%, but to avoid exceeding, the maximum number of days I can have a holiday from the lab should be 4.")