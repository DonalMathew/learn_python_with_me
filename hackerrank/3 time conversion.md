![[Pasted image 20241206180534.png]]

ans:
```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[(len(s)-2):len(s)] == "PM":
        a=int(s[0:2])
        if a==12:
            a=12
        elif a==0:
            a=str("00")
        else:
            a+=12
        s=str(a)+s[2:]
    
    elif s[(len(s)-2):len(s)] == "AM":
        a=int(s[0:2])
        if a==12:
            a=str("00")
            s=str(a)+s[2:]
        
            
        
    
    return s[:len(s)-2]
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

```