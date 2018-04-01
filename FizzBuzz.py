# FizzBuzz.py is a program to learn WHILE, IF, ELSE, ELIF, and % modulo (the remainder after dividing)
# It was written by Ian McLoughlin on 2018-02-01
# and is used by Colm for testing
# FizzBuzz: https://en.wikipedia.org/wiki/Fizz_buzz
# note the logic of if,else, then(represented by :) 

i = 1

while i <= 300: 
    if (i % 3 == 0) and (i % 5 ==0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:          
        print(i)
    i = i +1

