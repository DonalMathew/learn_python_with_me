```python
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

arr=[]
# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        arr.append(mountain_h)

    largest=max(arr)
    index=arr.index(largest)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(index)
    arr=[]

```

## sort
```python
# Example array
arr = [5, 2, 9, 1, 5, 6]

# Sort in ascending order
arr.sort()
print(arr)  # Output: [1, 2, 5, 5, 6, 9]
```

## rounding decimal points
```python
number = 3.141592653589793
rounded_number = round(number, 6)
print(rounded_number)  # Output: 3.141593
```


## sum
```python
# Example array
arr = [10, 20, 30, 40, 50, 60, 70]

# Using list comprehension to sum the first 5 elements
sum_first_five = sum(arr[i] for i in range(5))

print("Sum of the first 5 elements:", sum_first_five)  # Output: 150
```

