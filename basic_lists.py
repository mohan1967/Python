if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        get_input=input().split()
        if(str(get_input[0])=="insert"):
            l.insert(int(get_input[1]),int(get_input[2]))
        elif(str(get_input[0])=="pop"):
            l.pop()
        elif(str(get_input[0])=="reverse"):
            l.reverse()
        elif(str(get_input[0])=="print"):
            print(l)
        elif(str(get_input[0])=="remove"):
            l.remove(int(get_input[1]))
        elif(str(get_input[0])=="append"):
            l.append(int(get_input[1]))
        elif(str(get_input[0]=="sort")):
            l.sort()
        
        
            
            
            
            
        