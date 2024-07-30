
from SpiderNet import HashMap

# Adding key and value to HashMap
map=HashMap()
map.add('storage','github')
map.add('cost',22)

# Get value of a respective key 
key=map.value('cost') # returns 22
print(key)

# Get key of a respective value 
key=map.value(22) # returns 'cost'
print(key)

#Getting list of all keys and list of all values 
all_keys=map.keys()
all_values=map.values() 

#Getting the length of the HashMap
length=len(map) #returns the length of the hashmap

# The HashMap is also Iterable through the builtin ForEach Loop. Look at for_each.py

#You can also initialize the HashMap with an existing 'dict' datatype in python
map_2=HashMap({1:'a',2:'b'})
