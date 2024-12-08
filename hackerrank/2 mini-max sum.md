![[Pasted image 20241206112859.png]]

ans:
```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print(sum(arr[i] for i in range(4)),sum(arr[i] for i in range(1,5)))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
```

![[Pasted image 20241206113009.png]]