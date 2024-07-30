
# We can Initialize the Array , either leaving it empty or passing a list through it 
array=Array() #leave empty
# or
array=Array([1,2,3,"Name"])

#Adding values to the array
array.append(10) # adds 10 to the array 

# Get a value based on index provided
second_item=array.get(1) 

# Array is also iterable 
x=Array([1,2,3,4])
for y in x:
    print(y) 
# will print 1 2 3 4 5 in different lines
