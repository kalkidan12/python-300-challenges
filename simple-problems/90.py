#Q.90. Write a python program to get age of 10 student from user and store in a list.
# condition is that system should display age that greater than 14 year and lessthan 20 year.


student = []

for i in range(10):
    student.append(int(input('Enter the age of student here ')))
print([x for x in student if x>14 and x<20])