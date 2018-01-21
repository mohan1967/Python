def count_substring(string, sub_string):
    s=len(string)
    count=0
    for i in range(s):
        if(string[i:i+len(sub_string)]==sub_string):
            count+=1
    return count
        