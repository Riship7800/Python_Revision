############## LIST AND TUPLES ###############

# A built in datatype that stores set of values
marks = [94.4, 65.3, 85.2, 76.4, 44.3, 96.5, 34.9]
print(marks)
print(type(marks))
print(marks[0])

#It can store elements of different types(Integers, float, string, etc)
student = ["Rakesh", 24, "Delhi"]
print(student)

#Strings:tuples are immutable -- Lists are mutable
# str = "Hello"
# str[0] = "Hi"
# print(str)  #This operation is not allowed

student[0] = "Rushikesh"
print(student)


###List Slicing
print(marks[2:4])
print(marks[-6:-1])


###List Methods
list = [1, 2, 3, 4, 5, 6]   #Can also sort strings
list.append(4)  #Adds one element at the end
print(list)
list.sort()  #Sorts in ascending order
print(list)
list.sort(reverse=True)  #Sorts in decending order
print(list)
list.reverse()  #Reverses list
print(list)
list.insert(5,5)  #Insert element at index(index,element)
print(list)
list.remove(1)  #Removes first occurance of element
print(list)
list.pop(4)  #Removes element at index
print(list)


##### Tuples in Python  #####
#A built in data type that lets us create immutable sequences of values
#tup =() is also valid 
#tup = (1) will be considered as int, tup = ("Hello") will be considered string,, tup = (5.2) will be considered float
#to make a tupple tup = (1,) a comma is necessary to identify it as a tupple
tup = (34, 64, 89, 15, 65, 25, 38)
print(tup)

#Methods in tupple
print(tup.index(89)) #returns index of first occurance
print(tup.count(34)) #counts total occurances

# Practise Questions
# Write a program to ask the user to enter names of their 3 favourite movies and save them in a list
movies = []
movies.append(input("Enter movie1: "))
movies.append(input("Enter movie2: "))
movies.append(input("Enter movie3: "))
print(movies)

#Write a program to check if a list contains a palindrome of elements
list1 = [1 ,2 ,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("Palindrome")
else:
    print("Not a Palindrome")

#WAP to count the number of students with the "A" grade in the following tuple
list2 = ["C", "D", "A", "A", "B", "B", "A"]
print(list2.count("A"))
list2.sort()
print(list2)