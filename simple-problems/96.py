#Q.96. Write a python program to get 10 data item from user how much integer , float and string type of data is stored in a list.

my_list = [1,2.2,3,3.4,'kali', 'ideal', 23, 33.6, 'new', 90]
int_item, float_item, str_item = 0,0,0
for i in my_list:
    if(type(i)==int):
        int_item +=1
    if(type(i)==float):
        float_item +=1
    if(type(i)==str):
        str_item +=1
print(int_item)
print(float_item)
print(str_item)
   

# challenge
# Write a python program to get 10 float data item from user,system shoul convert float data type into integer.
float_list = [1.0,2.2,3.4,3.4,33.3, 55.5, 23.3, 33.6, 0.09, 90.1]
int_list = []
for i in float_list:
    to_int = int(i)
    int_list.append(to_int)
print(float_list)
print(int_list)

 
    