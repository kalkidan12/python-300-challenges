#Q.86. Write a python program to search any character  (or set of character ) from string

string = input('Enter set of character ')
print(string)
ch = input('Enter the character you want to search ')

if ch in string:
    print('yes')
else:
    print('not found')
