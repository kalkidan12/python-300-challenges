#102. Write a python program to display all student name except with start 'f' character.

student =  ['kalkidan', 'kalab', 'fkreab', 'daniel']
for i in student:
    if(not (i.startswith('f'))):
        print(i)
    

#challenge
#Write a python program to display all student name except with start 'f' and end with 'n' character.

#solution
print('===========')
for i in student:
    if(not i.startswith('f') and not i.endswith('n')):
        print(i)