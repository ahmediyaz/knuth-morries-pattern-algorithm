s=input()
p=input()
pt= [0]*len(p)#declaring empty list to store the pi table values 
j = 0   
c = 0
pt[0]
i = 1
while i < len(p):
    if p[i]== p[c]:
        c+= 1
        pt[i] = c
        i += 1
    else:
        if  c!= 0: 
            c = pt[c-1]
        else:
            pt[i] = 0
            i += 1
i = 0 
while i < len(s): 
    if p[j] == s[i]:
        i += 1
        j += 1
    if j == len(p):
        print("searching pattren avaliable at position in the given string is : " + str(i-j))
        j = pt[j-1] 
  
    elif i < len(s) and p[j] != s[i]: 
        if j != 0: 
            j = pt[j-1] 
        else:
            i += 1
  
    
  

  
