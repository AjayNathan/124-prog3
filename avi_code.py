# functions

import random
import math

def randnums(a,b,n,step=1):
    return [random.randrange(a,b,step) for x in range(n)]

def random_sample_res(s,A):
    res = 0
    for x,y in zip(s,A):
        res = res + x*y
    return abs(res)

def random_sample_move(S):
    i = randnums(0,len(S),1,1)[0]
    if random.random() > 0.5:
        j = randnums(0,len(S),1,1)[0]
        while i == j:
            j = randnums(0,len(S),1,1)[0]
        S[j] = -S[j]
    S[i] = -S[i]
    return S

def prepartition(A,P = False):
    n = len(A)
    if P == False:
        P = randnums(1,n+1,n)
    for i in range(0,n):
        for j in range(i+1,n):
            if P[i] == P[j]:
                A[i] += A[j]
                A[j] = 0
    return A,P

def prepartition_move(P):
    i = randnums(0,len(P),1,1)[0]
    j = randnums(0,len(P),1,1)[0]
    while i == j:
            j = randnums(0,len(P),1,1)[0]
    P[i] = j
    return P

def max_two(nums):
    a = 0
    b = 1
    if nums[0] < nums[1]:
        a = 1
        b = 0
    for i in xrange(len(nums)):
        if i > 1:
            if nums[i] > nums[a]:
                b = a
                a = i
            elif nums[i] > nums[b]:
                b = i
    return (a, b)

def kk(nums):
    for i in xrange(len(nums)):
        a, b = max_two(nums)
        nums[a] = nums[a] - nums[b]
        nums[b] = 0

    a, _ = max_two(nums)

    return nums[a]

def T(i):
    return 10**10*(0.8)**math.floor(i/300.0)

def calc_mean(l):
    s = 0
    for x in l:
        s += x
    return s/len(l)

# start of code
runs = 25000

kklist = []
rrs = []
rrpp = []
hcs = []
hcpp = []
sas = []
sapp = []


for _ in xrange(2):
    S = randnums(-1,2,100,2)
    A = randnums(1,10**12,100)

    kklist.append(kk(A[:]))

    # repeated random, standard

    bestres = 10**13
    currress = 10**13
    for x in xrange(runs):
        Sj = randnums(-1,2,100,2)
        currres = random_sample_res(Sj,A[:])
        if currres < bestres:
            bestres = currres

    rrs.append(bestres)

    # repeated random, preparition

    curr = kk(A[:])
    for x in xrange(runs):
        Aprime, P = prepartition(A[:])
        prev = kk(Aprime[:])
        if prev < curr:
            curr = prev

    rrpp.append(curr)

    # hill climb, standard

    SHi = S[:]
    bestreshill = 10**13
    currresshill = random_sample_res(SHi[:],A[:])
    for x in xrange(runs):
        SHi = random_sample_move(SHi[:])
        currreshill = random_sample_res(SHi[:],A[:])
        if currreshill < bestreshill:
            bestreshill = currreshill

    hcs.append(bestreshill)

    # hill climb, prepartition

    Ai, P = prepartition(A[:])
    currhill = kk(Ai[:])
    for x in xrange(runs):
        P = prepartition_move(P)
        App, P = prepartition(A[:],P)
        prevhill = kk(App)
        if prevhill < currhill:
            currhill = prevhill

    hcpp.append(currhill)

    # simple annealing, standard

    bestressa = random_sample_res(S[:],A[:])
    Spp = S[:]
    sppres = bestressa
    for x in xrange(runs):
        Sp = random_sample_move(S[:])
        currressa = random_sample_res(Sp[:],A[:])
        if currressa < bestressa:
            bestressa = currressa
        elif random.random() < math.e**(-(currressa-bestressa)/T(x)):
            bestressa = currressa
        if bestressa < sppres:
            sppres = bestressa

    sas.append(sppres)

    # simple annealing, pp

    Asa, Psa = prepartition(A[:])
    brsa = kk(Asa[:])
    appres = brsa
    for x in xrange(runs):
        Psa = prepartition_move(Psa[:])
        Apsa, Psa = prepartition(Asa[:],Psa[:])
        crsa = kk(Apsa[:])
        if crsa < brsa:
            brsa = crsa
        elif random.random() < math.e**(-(crsa-brsa)/T(x)):
            brsa = crsa
        if brsa < appres:
            appres = brsa

    sapp.append(appres)

# print "KK: ", kklist
# print "Repeated Random, Standard: ", rrs
# print "Repeated Random, PP: ", rrpp
# print "Hill climb, Standard: ", hcs
# print "Hill climb, PP: ", hcpp
# print "SA, Standard: ", sas
# print "SA, PP: ", sapp

print "KK: ", calc_mean(kklist)
print "Repeated Random, Standard: ", calc_mean(rrs)
print "Repeated Random, PP: ", calc_mean(rrpp)
print "Hill climb, Standard: ", calc_mean(hcs)
print "Hill climb, PP: ", calc_mean(hcpp)
print "SA, Standard: ", calc_mean(sas)
print "SA, PP: ", calc_mean(sapp)
