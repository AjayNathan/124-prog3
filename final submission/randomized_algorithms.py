# functions
import random
import math
import time

# generates random numbers
def randnums(a,b,n,step=1):
    return [random.randrange(a,b,step) for x in range(n)]

# residue for standard representation
def random_sample_res(s,A):
    res = 0
    for x,y in zip(s,A):
        res = res + x*y
    return abs(res)

# movement in standard
def random_sample_move(S):
    i = randnums(0,len(S),1,1)[0]
    if random.random() > 0.5:
        j = randnums(0,len(S),1,1)[0]
        while i == j:
            j = randnums(0,len(S),1,1)[0]
        S[j] = -S[j]
    S[i] = -S[i]
    return S

# prepartitions a list
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

# movement in prepartition
def prepartition_move(P):
    i = randnums(0,len(P),1,1)[0]
    j = randnums(0,len(P),1,1)[0]
    while i == j:
            j = randnums(0,len(P),1,1)[0]
    P[i] = j
    return P

# finds max two elements
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

# Karmarkar-Karp
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
    s = 0.0
    for x in l:
        s += x
    return s/len(l)

runs = 25000

kklist = []
rrs = []
rrpp = []
hcs = []
hcpp = []
sas = []
sapp = []

rrstimes = []
rrpptimes = []
hcstimes = []
hcpptimes = []
sastimes = []
sapptimes = []

for n in xrange(0, 50):
    S = randnums(-1,2,100,2)
    A = randnums(1,10**12,100)
    _ ,P = prepartition(A[:])

    kklist.append(kk(A[:]))

    # repeated random, standard

    otime = time.time()

    bestres = 10**13
    currress = 10**13
    for x in xrange(0,runs):
        Sj = randnums(-1,2,100,2)
        currres = random_sample_res(Sj,A[:])
        if currres < bestres:
            bestres = currres

    rrs.append(bestres)
    rrstimes.append(time.time() - otime)

    # repeated random, preparition

    otime = time.time()

    curr = kk(A[:])
    for x in xrange(0,runs):
        Aprime, P = prepartition(A[:])
        prev = kk(Aprime[:])
        if prev < curr:
            curr = prev

    rrpp.append(curr)
    rrpptimes.append(time.time() - otime)

    # hill climb, standard

    otime = time.time()

    SHi = S[:]
    bestreshill = 10**13
    currresshill = random_sample_res(SHi[:],A[:])
    for x in xrange(0,runs):
        SHi = random_sample_move(SHi[:])
        currreshill = random_sample_res(SHi[:],A[:])
        if currreshill < bestreshill:
            bestreshill = currreshill

    hcs.append(bestreshill)
    hcstimes.append(time.time() - otime)

    # hill climb, prepartition

    otime = time.time()

    Ai, Pi = prepartition(A[:],P[:])
    currhill = kk(Ai[:])
    for x in xrange(0,runs):
        Pi = prepartition_move(Pi[:])
        App, Pi = prepartition(A[:],Pi[:])
        prevhill = kk(App)
        if prevhill < currhill:
            currhill = prevhill

    hcpp.append(currhill)
    hcpptimes.append(time.time() - otime)

    # simulated annealing, standard

    otime = time.time()

    Spp = S[:]
    Sp = S[:]
    Sppres = random_sample_res(Spp[:],A[:])
    Sres = Sppres
    for x in xrange(0,runs):
        Sp = random_sample_move(Sp[:])
        Spres = random_sample_res(Sp[:],A[:])
        if Spres < Sres:
            Sres = Spres
        elif random.random() < math.e**(-(Spres-Sres)/T(x)):
            Sres = Spres
        if Sres < Sppres:
            Sppres = Sres

    sas.append(Sppres)
    sastimes.append(time.time() - otime)

    # simulated annealing, prepartition

    otime = time.time()

    Acopy, Pinit = prepartition(A[:],P[:])
    Sppres = kk(Acopy[:])
    Sres = Sppres
    Pp = Pinit
    for x in xrange(0,runs):
        Pp = prepartition_move(Pp[:])
        Ap,Pp = prepartition(A[:],Pp[:])
        Spres = kk(Ap[:])
        if Spres < Sres:
            Sres = Spres
        elif random.random() < math.e**(-(Spres-Sres)/T(x)):
            Sres = Spres
        if Sres < Sppres:
            Sppres = Sres

    sapp.append(Sppres)
    sapptimes.append(time.time() - otime)

# prints results

print "RESULTS"
print "--------------------------------"
print "KK: ", kklist
print "Repeated Random, Standard: ", rrs
print "Repeated Random, PP: ", rrpp
print "Hill climb, Standard: ", hcs
print "Hill climb, PP: ", hcpp
print "SA, Standard: ", sas
print "SA, PP: ", sapp

print "KK: ", calc_mean(kklist)
print "Repeated Random, Standard: ", calc_mean(rrs)
print "Repeated Random, PP: ", calc_mean(rrpp)
print "Hill climb, Standard: ", calc_mean(hcs)
print "Hill climb, PP: ",calc_mean(hcpp)
print "SA, Standard: ", calc_mean(sas)
print "SA, PP: ", calc_mean(sapp)

print "TIMES"
print "---------------------------------"
print "Repeated Random, Standard: ", rrstimes
print "Repeated Random, PP: ", rrpptimes
print "Hill climb, Standard: ", hcstimes
print "Hill climb, PP: ", hcpptimes
print "SA, Standard: ", sastimes
print "SA, PP: ", sapptimes

print "Repeated Random, Standard: ", calc_mean(rrstimes)
print "Repeated Random, PP: ", calc_mean(rrpptimes)
print "Hill climb, Standard: ", calc_mean(hcstimes)
print "Hill climb, PP: ",calc_mean(hcpptimes)
print "SA, Standard: ", calc_mean(sastimes)
print "SA, PP: ", calc_mean(sapptimes)
