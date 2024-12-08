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


same code in javascript:
```js
function twoLargest(arr) {
    let fst = 0;
    let sec = 0;
    
    for (let x of arr) {
        if (x > fst) {
            sec = fst;
            fst = x;
        } else if (x > sec && x !== fst) {
            sec = x;
        }
    }
    
    return [fst, sec];
}

function occurrences(arr, fst, sec) {
    let countf = 0;
    let counts = 0;

    for (let x of arr) {
        if (x === fst) {
            countf++;
        } else if (x === sec) {
            counts++;
        }
    }

    return [countf, counts];
}

const arr = [1, 2, 3, 5, 3, 5, 2, 5, 5];
const [fst, sec] = twoLargest(arr);
console.log(`Two largest numbers: ${fst}, ${sec}`);

const [countf, counts] = occurrences(arr, fst, sec);
console.log((countf - 1) + (counts - 1));

```