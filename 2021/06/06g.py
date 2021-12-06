G,F = map(int,open('i').read().split(",")),[0]*9
for f in G: F[f]+=1
for s in [80,176]:
    for z in range(s):
        F.append(F.pop(0))
        F[6] += F[8]
    print(sum(F))