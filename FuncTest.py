# by Colm Doherty 2018-4-17 to test possible scripts for creating a series of generic
# functions to simplify the existing NumpyData.py

# find the mean of the values in Column # when all rows are included

import numpy as np
# import the dataset
data = np.genfromtxt('Data/Iris.csv', delimiter=',')
# FOR TESTING - the existing organic code (it works):
col1mean = (np.mean(data[:,0]))
print("Column 1 mean is:",'{:0.3f}'.format(col1mean))

#define the new function for column mean.
def colmean(colno):
    meancol = (np.mean(data[:,colno]))
    return meancol    

print("Column 1 mean is:",'{:0.3f}'.format(colmean(0)))
print("Column 2 mean is:",'{:0.3f}'.format(colmean(1)))
print("Column 3 mean is:",'{:0.3f}'.format(colmean(2)))
print("Column 4 mean is:",'{:0.3f}'.format(colmean(3)))

# YAY! this took over 2hrs of trial & error to get right, with help from Ian's "Defining functions" video
# and a helluva of lotta noodling back & forth

# Another possible method - untested so far:
# def colmean = (np.mean(data[r,c]))
    # where r = row number, and c = column number
    # print("mean of column [c] for range in row[r] is: ")

#define the new function for column max:
def colmax(colno):
    maxcol = (np.max(data[:,colno]))
    return maxcol    

print("Column 1 max is:",'{:0.1f}'.format(colmax(0)))
print("Column 2 max is:",'{:0.1f}'.format(colmax(1)))
print("Column 3 max is:",'{:0.1f}'.format(colmax(2)))
print("Column 4 max is:",'{:0.1f}'.format(colmax(3)))


col1max = (np.max(data[:,0]))
    # find the max of the values in Column 1 (guessed this, since .mean gave the mean
col2max = (np.max(data[:,1]))
col3max = (np.max(data[:,2]))
col4max = (np.max(data[:,3]))  
print("Column 1 max is:",'{:0.3f}'.format(col1max))
    # display the Column 1 max to 3 decimal places 
print("Column 2 max is:",'{:0.3f}'.format(col2max))
print("Column 3 max is:",'{:0.3f}'.format(col3max))
print("Column 4 max is:",'{:0.3f}'.format(col4max))    
