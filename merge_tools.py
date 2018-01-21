def merge_the_tools(string, k):
    n=len(string)//k
    t=[]
    z=0
    for i in range(n):
        j=k*i
        m=(i+1)*k
        t.insert(z,string[j:m])
        z+=1
    
    for i in range(n):
        temp=t[i]
        print(''.join(sorted(set(temp),key=temp.index)))