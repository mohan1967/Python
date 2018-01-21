m=int(input())
a=list(map(int,input().split()))
b=set()
c=set()
for i in a:
    if i in b:
        c.add(i)
    else:
        b.add(i)
d=b-c
print(sum(d))
    
    