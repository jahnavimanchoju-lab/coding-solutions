# cook your dish here
N,m=map(int,input().split())
result=1
for i in range(m):
    result=N*result
print(result)