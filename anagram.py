'''
Created on Jan 31, 2016

@author: SharanyaVR
'''

def permuteString(lst):
    if(len(lst) == 0):
        return []
    elif(len(lst)== 1):
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):            
            x = lst[i];
            xs = lst[:i] + lst[i+1:]
            for p in permuteString(xs):
                l.append([x]+p)
        return l

def printAnagrams(word):
    file = open("anagram_out.txt","w")
    lst = permuteString(list(word))
    lst.sort()
    for p in lst:
        file.write(''.join(p)+"\n")
        file.flush()
    file.close() 
            
printAnagrams('Ron')