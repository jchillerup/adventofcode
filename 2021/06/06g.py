G,F,R = map(int,open('i').read().split(",")),[0]*9,range
for f in G: F[f]+=1

def G(v):
    v.append(v.pop(0))
    v[6] += v[8]

for s in [80,176]:
    for z in range(s):G(F)
    print(sum(F))