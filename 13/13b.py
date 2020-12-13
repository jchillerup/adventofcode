import math
import functools 

current_time, busses = open('input.txt').read().strip().split("\n")
current_time = int(current_time)
busses = busses.split(",")

def get_equations(it):
    for idx, freq in enumerate(it):
        if freq != 'x':
            yield (-idx % int(freq), int(freq))

# Stolen from here: https://github.com/MartinThoma/LaTeX-examples/blob/master/source-code/Pseudocode/SolveLinearCongruences/solveLinearCongruences.py
def ExtendedEuclideanAlgorithm(a, b):
    aO, bO = a, b

    x = lasty = 0
    y = lastx = 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return {"x": lastx, "y": lasty, "gcd": aO * lastx + bO * lasty}


def solveLinearCongruenceEquations(rests, modulos):
    assert len(rests) == len(modulos)
    x = 0
    M = functools.reduce(lambda x, y: x * y, modulos)

    for mi, resti in zip(modulos, rests):
        Mi = M // mi
        s = ExtendedEuclideanAlgorithm(Mi, mi)["x"]
        e = s * Mi
        x += resti * e
    return {"congruence class": ((x % M) + M) % M, "modulo": M}


equations = sorted(get_equations(busses), key=lambda x: x[1], reverse=True)

rests = [x[0] for x in equations]
modulos = [x[1] for x in equations]

print(solveLinearCongruenceEquations(rests, modulos)["congruence class"])