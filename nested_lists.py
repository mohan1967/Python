if __name__ == '__main__':
    maxscore=[]
    temp=[]
    ans=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        maxscore.append((name,score))
    for i in range(len(maxscore)):
        temp.append(maxscore[i][1])
    u=sorted(list(set(temp)))[1]
    
    for i in range(len(maxscore)):
        if(u==maxscore[i][1]):
            ans.append(maxscore[i][0])
            
    answer=[]
    answer=sorted(list(set(ans)))
    for i in range(len(answer)):
        print(answer[i])
        
