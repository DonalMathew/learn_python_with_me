![[Pasted image 20241205144250.png]]

```python

def twolargest(arr):
    fst=0
    sec=0
    for x in arr:
        if(x>fst):
            sec=fst
            fst=x
        elif(x>sec and x!=fst):
            sec=x
    return fst,sec

def occurences(arr):
    countf,counts=0,0
    for x in arr:
        if(x==fst):
            countf+=1
        elif(x==sec):
            counts+=1
    return countf,counts


arr=[1,2,3,5,3,5,2,5,5]
print(twolargest(arr))
fst,sec=twolargest(arr)

countf,counts=occurences(arr)
print((countf-1)+(counts-1))


```