import numpy as np

def sign(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1

def line(p1, p2):
    slope = np.array((sign(p2[0]-p1[0]), sign(p2[1]-p1[1])))
    
    ptr = p1
    while not np.all(ptr == p2):
        yield(ptr)
        ptr += slope
    yield(p2)

def draw_line(i, diagonal=False):
    p1,p2 = [np.array((int(x), int(y))) for x,y in [x.split(",") for x in i.split(" -> ")]]
    
    if not diagonal:
        if not (p1[0] == p2[0] or p1[1] == p2[1]): return
    
    for point in line(p1, p2):
        map[tuple(point)] += 1

map = np.zeros((1000, 1000))
q1 = [draw_line(x) for x in open('input.txt').read().strip().split("\n")]
print(np.sum(map >= 2))

map = np.zeros((1000, 1000))
q2 = [draw_line(x, True) for x in open('input.txt').read().strip().split("\n")]
print(np.sum(map >= 2))