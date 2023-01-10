#102. Write a python program to sort student name in ascending order in list and student should display which contain only 5 characters.

student = ['kalkidan', 'kalab', 'fkreab', 'daniel']
student.sort()
fived = []
#sort and display the list iteme which length is equal to 5
for i in student:
    if(len(i) == 5):
        fived.append(i)
print(fived)
        
        
        
# challenge

# Write a python program to sort student name in decending order in list and put A '.' at the end of every student name add '.' at end of every list item

#aolution
student.sort(reverse=True)
for i in range(len(student)):
    student[i] = student[i]+'.'
    
    
       
print(student)

