#Q.95. Write a python program to get number from user to display table in reverse order.
# 2 * 10 = 20
# 2 * 9 = 18
# 2 * 8 = 16

num = int(input("Enter Number "))
for i in range(10,0,-1):
    
    print(str(num) + " * " + str(i) + " = " + str(num*i))


print("================================")
#challenge
# Write a python program to get number from user to display table in reverse order, number should multiply wuth odd number only.
for i in range(10,0,-1):
    if(i%2 != 0):
        print(str(num) + " * " + str(i) + " = " + str(num*i))
    

