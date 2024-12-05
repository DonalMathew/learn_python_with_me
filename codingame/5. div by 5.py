# Write a Python code to display numbers from a list divisible by 5

def div(list):
    list1=[]
    for i in list:
        if(i%5==0):
            list1.append(i)
    return list1

list=[1,5,10]
print(div(list))
