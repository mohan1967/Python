def minion_game(string):
    countk=0
    counts=0
    vowels="AEIOU"
    for i in range(len(string)):
        if s[i] in vowels:
            countk=countk+(len(s)-i)
        else:
            counts=counts+(len(s)-i)
    if(countk==counts):
        print("Draw")
    elif(countk>counts):
        print("Kevin", countk)
    else:
        print("Stuart", counts)