# LPYAS71

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that takes three space separated numbers as input and prints:

- "Increasing" if the numbers are in strictly increasing order,
- "Decreasing" if they are in strictly decreasing order,
- and "Neither" otherwise.

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
20 30 41
```

```
Increasing
```

### Sample 2:
Input
Output

```
50 30 20
```

```
Decreasing
```

### Sample 3:
Input
Output

```
23 42 30
```

```
Neither
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T15:17:48.524Z  

```py
# cook your dish here
n,y,z=map(int,input().split())
if n>y>z:
    print("decreasing")
elif n<y<z:
    print("increasing")
else:
    print("neither")
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS71)