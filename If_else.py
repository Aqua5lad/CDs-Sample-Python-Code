# Adapted from : https://docs.python.org/3/tutorial/controlflow.html
# by Colm Doherty in Feb 2018 and updated on Apr 1st 2018
# Purpose is to understand if, elif and else statements 

x = int(input("Please enter an integer: "))
if x < 0:
  x = 0
  print('Negative changed to zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')
