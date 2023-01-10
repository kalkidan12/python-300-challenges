#Q.99. Write a python program to get only uppercase word from user store in a list

upper_list = []

for i in range(10):
    w = input('write word in upper case' )
    if (w.isupper()):
        upper_list.append(w)
    else:
        print("error! insert only uppercase word")
print(upper_list)


#challenge
#99. Write a python program to get only lowercase word from user store in a list

lower_list = []

for i in range(10):
    w = input('write word in lower case ')
    if (w.islower()):
        lower_list.append(w)
    else:
        print("error! insert only lowercase word")
print(lower_list)
    

