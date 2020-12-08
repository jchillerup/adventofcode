

groups = open('input.txt', 'r').read().strip().split("\n\n")

#1 
s=0
for g in groups:
    
    participants = [x.strip() for x in g.strip().split("\n")]
    g_set = set()

    for p in participants:
        g_set.update(set(list(p)))

    s += len(g_set)
print(s)

# 2
s=0
for g in groups:
    
    participants = [x.strip() for x in g.strip().split("\n")]
    g_set = set(participants[0])

    for p in participants:
        g_set = g_set.intersection(set(list(p)))

    s += len(g_set)
print(s)