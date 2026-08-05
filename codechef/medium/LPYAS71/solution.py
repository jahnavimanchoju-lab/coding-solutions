# cook your dish here
n,y,z=map(int,input().split())
if n>y>z:
    print("decreasing")
elif n<y<z:
    print("increasing")
else:
    print("neither")