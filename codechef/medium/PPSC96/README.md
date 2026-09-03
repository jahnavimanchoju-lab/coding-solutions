# PPSC96

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Power of a Number

Listen

You are given 2 space separated integers $N$ and $m$.

You need to output the value $N^m$.
Check the sample output given below.

### Sample 1:
Input
Output

```
5 3
```

```
125
```

### Sample 2:
Input
Output

```
8 4
```

```
4096
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T15:51:13.133Z  

```py
# cook your dish here
N,m=map(int,input().split())
result=1
for i in range(m):
    result=N*result
print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC96)