#Q.87. Write a python program to get a sentence from user , the system should  display 
# only ten character maximum.

sentence  = str(input('Enter sentence here '))


print(sentence[slice(0,10)])
# or
print(sentence[0:10], end='')


    