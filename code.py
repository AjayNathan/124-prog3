import random

def randnums(a,b,n,step=1):
    return [random.randrange(a,b,step) for x in range(n)]

def random_sample_res(S,A):
    res = 0
    for x,y in zip(S,A):
        res += x*y
    return res

S = randnums(-1,2,4,2)
A = randnums(1,14,4,1)

def random_sample_move(S):
    i = randnums(0,len(S),1,1)[0]
    if random.random() > 0.5:
        print "also switching j"
        j = randnums(0,len(S),1,1)[0]
        while i == j:
            j = randnums(0,len(S),1,1)[0]
        S[j] = -S[j]
    S[i] = -S[i]
    return S

def prepartition(A):
    n = len(A)
    P = randnums(1,n+1,n)
    print P
    for i in range(0,n):
        for j in range(i+1,n):
            if P[i] == P[j]:
                A[i] += A[j]
                A[j] = 0
                print A
    return A,P

def prepartition_move(P):
    i = randnums(0,len(P),1,1)[0]
    j = randnums(0,len(P),1,1)[0]
    while i == j:
            j = randnums(0,len(P),1,1)[0]
    P[i] = j
    return P
