#Strings

#Three types of ways to write string
str1 = "This is string1"
str2 = 'This is string2'
str3 = '''This is a string'''


#string Manuplation
new1 = "Hello i am Revising python \n i am rushikesh" #\n is used for new line and \t is used for yab space
print (new1)


###     String Operations   ###
#Concatenation
str3 = str1+" "+str2
print (str1+" "+str2)
print (str3)

#Length of string
print (len(str1)) #length is a Function



###     Indexig     ###
#When we input a string each character is assigned a number for its position
# EG - Hello so here H gets position 0, e gets 1, l gets 2 and so on (Empty spaces are also given index)
#helps to access characters
new_str = "This is Python"
ch = new_str[1]
print (ch)  #prints character y as its position is 1 



###     Slicing     ###
#Accessing part of a string
#to get at the end of string you need to +1 th index end value
ch1 = new_str[1:4]
ch2 = new_str[:4] #python know that we want to start from 0 so it prints from 0 to 4
ch3 = new_str[3:] #python kows that we want to go to end of string so it prints from 3 to 6
print (ch1) #print yth from positon 1 to 3 will not print o from 4th position
print (ch2)
print (ch3)
#Theres also negative indexing in slicing
#p      y       t       h        o       n
#-6    -5      -4      -3       -2      -1 
# negative indexing starts from end of string and with -1  
ch4 = new_str[-4:-1]
print (ch4)



###     String Functions        ###
print (new_str.endswith("on")) #To check if particular string ends with specific characters
print (new_str.capitalize) #Capitalizes the first character of the string, will create a new string and if we print the original string will be printed as it is without cipatalization
print (new_str.replace("i","e")) #replaces specific characters from the string
print (new_str.replace("Python","Javascript"))
print (new_str.find("o")) #where the first time it occurs it return its 1st index
print (new_str.find("is")) #if the character or word dosent exist it returns -1
print (new_str.count("i")) #counts the occurance of the substring, i occurs 2 times





#######                 Practise                ######
# Write a program to inputs users first name & print its length
name = input ("Enter your name:")
print (name)

# Write a program to find the occurrence of "$ in a string"
new_str2 = "$this is $revision of $ python"
print (new_str2.count("$"))



###      Conditional Statements      ###
# If else If
age = 21
if(age>18):
    print("You are eligible for Vote")
elif(age == 18):
    print("You just became eligible")
else:
    print("You are not eligible")

# Nesting in conditional statements
if(age>18):
    if(age>80):
        print ("cannot drive")
    else:
        print ("Can drive")
else:
    print ("You are still a baby")




####                Practisee               ####
# WAP to check is the entered number is even or odd
num = int(input("Enter the number"))
if(num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")

# WAP to find the greatest number of the 3 mubers entered by the user
num1 = 5
num2 = 8
num3 = 3
if(num1>num2 & num1>num3):
    print("num1 is the greatest")
elif(num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")


