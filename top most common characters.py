
#!/bin/python3

from collections import OrderedDict
import sys

if __name__ == "__main__":
    s = list(' '.join(input().strip().split()))    
    d = dict()        
    d2= OrderedDict()

    for x in s:
        if x in d:
            d[x]=d[x]+1
        else:
            d[x]=1    
    
    vals = list(set(list(d.values())))    
    vals.sort(reverse=True)    
    for k in vals:        
        l=[]
        for x in d:
            if k == d[x]:
                l.append(x)
        l.sort()
        for c in l:
            d2[c]=k 
  
    i=0
    for v in d2:
        if i <3:
            print(v,d2[v])
            i+=1
          
        