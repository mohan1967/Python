n = int(input())
s = set(map(int, input().split())) 
m=int(input())
a=[]
for i in range(m):
    a=input().split()
    if(a[0]=='remove'):
        s.remove(int(a[1]))
    elif(a[0]=='discard'):
        s.discard(int(a[1]))
    else:
        s.pop()
print(sum(s))

