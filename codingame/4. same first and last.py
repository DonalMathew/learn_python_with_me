# Write a code to return True if the list’s 
# first and last numbers are the same. If the numbers are different, return False.

def same(list):
    if(list[0]==list[-1]):
        return True
    else:
        return False

list=[1,2,3]
print(same(list))