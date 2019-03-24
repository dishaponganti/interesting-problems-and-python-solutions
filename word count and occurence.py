from collections import OrderedDict 

myorder = OrderedDict()
for i in range(int(input().strip())):
    name = input()
    if name not in myorder:
        myorder[name]=1
    else:
        myorder[name]=myorder[name]+1
print(len(myorder))        
for v in myorder:
    print(myorder[v],end=' ')