from collections import defaultdict as D
G,F,R = map(int,open('i').read().split(",")),D(int),range
for f in G: F[f]+=1

def L(v):
    x = v[0]
    for i in R(9): 
        v[i]=v[(i+1)]
    v[6]+=x
    v[8]=x

for s in [80,176]:
    for z in range(s):L(F)
    print(sum(F.values()))