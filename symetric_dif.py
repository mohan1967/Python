int(input())
m=set(input().split())
int(input())
n=set(input().split())
print(*sorted((m^n),key=int),sep='\n')