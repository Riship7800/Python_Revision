##########      Dictionary & Sets       #############

###Disctionary in python - Dictionaries are used to store data values in key:value pairs
# dict = {
#     "name" : "Rishi",
#     "Cgpa" : 7.0,
# }
# Dictionarys are unordered as there are no indexes, mutable, dont allow duplicate

info = {
   "name" : "Rishi",
   "Cgpa" : 7.0,
   "learning" : "coding",
   "Coding" : ["C", "Python", "Java"],
   "topics" : ("Dictionary", "Sets"),
   "is_adult" : True,
   11.9 : 12
}
print(info)
print(info["Cgpa"])
info["name"] = "Rushikesh"
info["is_adult"] = False
print(info)

#Dictionary Methods
info.keys() #returns all keys
info.values() #returns all values
info.items() #return all key:value pairs as tuples
info.get("key") #returns the key according to value
info.update() # inserts the specified items to the dictionary


### Sets - Sets is the collection of the unordered items
#each element in the set must be unique & immutable
nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}  # repeated elements stored only once, so its resolved to {1,2} 
collection = {1, 2, 3, 2, "Hello", "one", "one"}
print(collection) # duplicate values are not printed 
print(type(collection)) 
print(len(collection))  # duplicate values are ignored in sets
null_set = set()  # empty set syntax

#Set Methods
nums.add(5) #Adds element
nums.add((1,2,3))
print(nums)
nums.remove(4) #removes the element
print(nums)
nums.pop()  #removes a random value
print(nums)
nums.union(set2) #combines both set values & returns new
print(nums)
print(nums.intersection(set2))
nums.clear()   # empties the set
print(nums)