#Q.93. Write a python program to find acceleration of man on a object having velocity v in in time t.
# formula a=v/s.

vf = float(input('Enter the final velocity '))
vi = float(input('Enter the initial velocity '))
t = float(input('Enter the time in seconds '))

change_velocity = vf-vi
a = change_velocity/t
print(f"force equals to: {a}")
