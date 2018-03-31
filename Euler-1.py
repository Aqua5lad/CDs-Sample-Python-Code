# Project Euler Problem 1, as solved by Ian McLoughlin on 2018-02-09

sum = 0
i = 1

while i < 1000:
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
    i = i + 1

print ("the sum of multiples of 3 and 5, less than 1000, is:", sum)    
