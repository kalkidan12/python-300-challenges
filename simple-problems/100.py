#Q.100. Write a python program to add number from list that are greater than 5 and lessthan 10.

numbers = [1,2,3,4,5,6,7,8,11,22,33,55]

sum = 0
for i in numbers:
    if(i>5 and i<10):
        sum +=i
print(sum)


#challenge 
# write a program to add even number from list
evenTotal = 0
for i in numbers:
    if(i%2 == 0):
        evenTotal +=i
print(evenTotal)
        