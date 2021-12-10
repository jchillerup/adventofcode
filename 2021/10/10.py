def f2(line):
    S,O,C,P,Q="","([{<",")]}>",[3,57,1197,25137],[1,2,3,4]
    for char in line:
        if char in O: S+=char
        else:
            if S[-1] == O[C.index(char)]:
                S=S[:-1]
            else:
                return (P[C.index(char)],0)
    
    if len(S) > 0:
        P=0
        for D in S[::-1]:
            P = P*5 + Q[O.index(D)]
        return (0,P)

a = [f2(y) for y in [x.strip()for x in open('input.txt').readlines()]]

print(sum([x[0] for x in a]))
q2 = sorted(x[1] for x in a if x[1]>0)
print(q2[len(q2)//2])