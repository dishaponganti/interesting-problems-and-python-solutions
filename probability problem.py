from itertools import groupby

def fact(x):
    if x ==0:
        return 1
    if x<=2 and x>0:
        return x
    res = 1
    for i in range(1,x+1):
        res = res * i
    #print("fac of ",x,"=",res)
    return res

def combs(n,r):
    #print("r= ",r)
    return fact(n)/(fact(n-r)*fact(r))

if __name__=="__main__":
    n = int(input().strip())
    vals = input().strip().split()
    vals.sort()
    N = int(input().strip())
    if len([len(list(g)) for k,g in groupby(vals) if k=='a'])!=0:
        a = [len(list(g)) for k,g in groupby(vals) if k=='a'][0]
        #print("a=", a)
        sum = 0

        if a == 0:
            print("{0:.3f}".format(float(0.000)))
        elif a == n:
            print("{0:.3f}".format(float(1.000)))
        else:
            for i in range(1, N + 1):
                if i <= a:
                    # print(a,"comb",i," * ",(n-a),"comb",(N-i),"  +  ")
                    sum = sum + combs(a, i) * combs((n - a), (N - i))
            print("{0:.3f}".format(sum / combs(n, N)))
    else:
        print("{0:.3f}".format(float(0.000)))