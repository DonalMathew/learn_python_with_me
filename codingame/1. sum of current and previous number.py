# https://pynative.com/python-basic-exercise-for-beginners/

# Write a Python code to iterate the first 10 numbers, 
# and in each iteration, print the sum of 
# the current and previous number.

a=[0,1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    print(f" for {i}, sum is {a[i-1]+a[i]}\n")