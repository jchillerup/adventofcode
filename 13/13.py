current_time, busses = open('input.txt').read().strip().split("\n")
current_time = int(current_time)
busses = busses.split(",")

def translate(x):
    if x != 'x':
        x = int(x)
        return current_time % x - x
    else:
        return 'x'

def int2(x):
    if x == 'x': return -1
    return int(x)

def max2(iter):
    cur_max = -99999999999999999999999999999
    cur_arg = -1
    for i, v in enumerate(iter):
        if v == 'x': continue
        if v > cur_max:
            cur_max = v
            cur_arg = i

    return cur_max, cur_arg

neg_wait, bus_id = max2(map(translate, busses))
bus = int(busses[bus_id])
print(bus*neg_wait*-1)
