############        Loops in Python         ################
# Loops are used to repeat instructions

# While loops
# while True :
#     print("hello")

count = 1   # count is iterator
while count <= 5 :  #Until the condition reaches false it will keep running
    print("Hello",  count)
    count += 1

print(count)    # will print the value of count that was at the end of execution

## Practise Questios

# Print numbers from 1 to 100
i = 1
while i <= 100 :
    print(i)
    i += 1

# Print numbers from 100 to 1
j = 100
while j >= 1 :
    print(j)
    j -= 1

# Print the multiplication table of a number n
n = int(input("Enter a number :"))
t = 1
while t <= 10 :
    print(n*t)
    t += 1

# Print thee elements of the following [1,4,9,16,25,36,49,64,81,100]
a = 1
while a <= 10 :
    print(a**2)
    a += 1

nums = [1,4,9,16,25,36,49,64,81,100] 
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# Search for the number x in the tuple using loop
b = int(input("Enter the number to search :"))
nums = (1,4,9,16,25,36,49,64,81,100)
indx = 0
while indx < len(nums) :
    if(nums[indx] == b):
        print("found at :",indx)
    indx += 1


####                         For loops
# for el in list :
#   some work

# for loop with else
# for el in list
#   some work
# else:
#   work when loop ends

list = [1,2,3,4]
for val in list :
    print(val)
else:
    print("Loop ended")

# Practise Questions
#Write a program to print the elements of the `list` using for loop
newlist = [1,4,9,16,25,36,49,64,81,100]
for i in newlist :
    print(i) 

#Search for the number x in the tuple using loop
x = int(input("Enter the number to search :"))
newtuple = (1,4,9,16,25,36,49,64,81,100)
for j in newtuple :
    if(j == x):
        print("Found at", newtuple.index(j))
    j += 1


### Range function
# range(start?, stop, step?)
# Rangee function returns a sequence of numbers starting from 0 (by default) to stop-1, incrementing by step (by default 1)
for ele in range(5) :  # will print 0 to 4
    print(ele)

for ele in range(1, 11) :  # will print 1 to 10, start and end are specified(1,11)
    print(ele)

seq = range(10)
for s in seq :
    print(s)

for ele in range(1, 11, 2) :  # will print odd numbers from 1 to 10, start at 1 stop att 11 and stepup is 2
    print(ele)

# Pass statement
# Pass is a null statement that does nothing. It is used as a placceholder for future code.
for el in range(5):
    pass


# Practise Questions
#WAP to find su of the first n natural numbers using while loop
n = int(input("Enter a number :"))
sum = 0
for i in range(1, n+1) :
    sum += n
    n -= 1
print(sum)

#WAP to find the factorial of a number using for loop
fac = int(input("Enter a number for factorial :"))
sum = 1
for i in range(1, fac+1) :
    sum *= i
print(sum)