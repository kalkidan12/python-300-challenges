#Q.90. Write a python program to generate a number from 0 to 20 only even number and generate 0 to 20 only add number.
# add both generated to each other to display total result.
evensum = 0
oddsum = 0
for x in range(0,21):
    if x%2==0:
        evensum +=x
    if x%2 !=0:
        oddsum +=x
total = evensum + oddsum
print(total)
        