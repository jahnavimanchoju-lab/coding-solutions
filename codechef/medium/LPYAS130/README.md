# LPYAS130

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that uses a for-each loop to print the square of each element in list of $N$ space separated integers, but skips elements greater than $10$.

Check the sample input and output below for further clarity.

 **Note** : Output the square of each element on a new line.

### Sample 1:
Input
Output

```
2 10 12 6 15
```

```
4
100
36
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T15:52:01.877Z  

```py
values = list(map(int, input().split()))
# Update your code below this line
for x in values:
    if x<=10:
        print(x*x)
        
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS130)