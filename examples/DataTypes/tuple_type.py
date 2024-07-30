from SpiderWeb import Tuple
# We can Initialize the tuple , either leaving it empty or passing a list through it 
tuple=Tuple() #leave empty
# or
tuple=Tuple([1,2,3,"Name"])

#Adding values to the tuple
tuple.append(10) # adds 10 to the tuple 

# Get a value based on index provided
second_item=tuple.get(1) 

# Tuple is also iterable 
x=Tuple((1,2,3,4))
for y in x:
    print(y) 
# will print 1 2 3 4 5 in different lines
