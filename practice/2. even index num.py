# Write a Python code to accept a string from the user
#  and display characters present at an even index number.

# For example, str = "PYnative". 
# so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

def even(str):
    for i in range(0,len(str),2):
        print(str[i])

str="Pynative"
even(str)