A=set(map(int,input().split()))
n=int(input())
print(all(A > set(map(int,input().split())) for _ in range(n)))
