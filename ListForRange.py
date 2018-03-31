# Colm Doherty 2018-02-21
# These are chunks of code I've written to test the List, For & Range functions
# they are tested & proven to work!

# here are some Lists, showing indexing & len(gth) (ie. number of items) 

Beatles = ['John', 'Paul', 'George', 'Ringo']
print ("the third Beatle was", Beatles[-2])
print ("the number of Beatles was:", len(Beatles))

homes = [55,13,19,58,7,21,86,190,2,49,219,55]
print ("the numbers of homes I've lived in are:", homes)
print ("the number of the third home I lived at was", homes[2])

for j in homes:
    print ("my home numbers, in sequence:", j)
    
for i in range(2,219,11):
    print (i)

for k in range(len(Beatles)):
    print (k, Beatles[k])

for s in Beatles:
    print (s)

for s in homes:
    print (s)

# script will go through the list and give the index position, then value, of each list in sequence      
l = 0
while l < len(homes):
    print (l, homes[l])
    l = l + 1
    
# script will go through the list and, for the word it's currently at, will give the length of that word     
for m in Beatles:
    print(m,len(m))
# unlike using "while" - it cannot show the index position of each word, because as it loops through, the value of 'm' keeps changing
# but there is a way to do it:

for m in range(len(Beatles)):
    print(m, Beatles[m], len(Beatles[m]))
