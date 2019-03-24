#!/bin/python3

import sys

def MergeBig(A,L,R):    
    i = 0
    j = 0
    k = 0
    
    while i<len(L) and j<len(R):        
        if len(L[i]) < len(R[j]):
            A[k] = L[i]
            i+=1
            k+=1       
        elif len(L[i]) > len(R[j]):
            A[k] = R[j]
            j+=1
            k+=1
        elif len(L[i]) == len(R[j]) and len(L[i])>(2**32):            
            w1 = list(map(int,L[i]))
            w2 = list(map(int,R[j]))
            x = 0            
            while x<len(w1):
                if int(w1[x])-int(w2[x])>0:
                    A[k] = R[j]
                    j+=1
                    k+=1
                    break
                elif int(w1[x])-int(w2[x])<0:
                    A[k] = L[i]
                    i+=1
                    k+=1
                    break                                    
                else:                       
                    x+=1                                        
                    if(x>=len(w1)):
                        A[k] = R[j]
                        j+=1
                        k+=1
                        break      
        elif len(L[i]) == len(R[j]) and len(L[i])<=(2**32):                                   
            if L[i] < R[j]:
                A[k] = L[i]
                i+=1
                k+=1       
            else:
                A[k] = R[j]
                j+=1
                k+=1
    while i <len(L):
        A[k] = L[i]
        i+=1
        k+=1
    while j <len(R):
        A[k] = R[j]
        j+=1
        k+=1            

def MergeSortBig(A):
    if len(A)<2:
        return
    m = len(A)//2
    L = A[:m]
    R = A[m:]
    MergeSortBig(L)
    MergeSortBig(R)
    MergeBig(A,L,R)
        
def bigSorting(arr):    
    MergeSortBig(arr)    
    print ("\n".join(map(str, arr)))
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = []    
    arr_i = 0
    for arr_i in range(n):
        arr_t = str(input().strip())        
        arr.append(arr_t)        
    bigSorting(arr)       
