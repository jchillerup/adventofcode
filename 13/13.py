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
del bus

#### PART 2

# from here: https://www.techiedelight.com/extended-euclidean-algorithm-implementation/
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)

def get_equations(it):
    for idx, freq in enumerate(it):
        if freq != 'x':
            yield (-idx % int(freq), int(freq))

equations = sorted(get_equations(busses), key=lambda x: x[1], reverse=True)

for congruent, modulo in equations:
    print("x = %d * j + %d" % (modulo, congruent) )


exit()
max_modulo = 1
for bus_idx, bus_frequency in enumerate(busses):
    if bus_frequency == 'x': continue
    
    bus_frequency = int(bus_frequency)

    #print("t+%d = 0 %% %d" % (bus_idx, bus_frequency))
    print("t = %d %% %d" % (-bus_idx%bus_frequency, bus_frequency))
    
    # <=> t + %d = 0 %% %d\t <=> t = %d (mod %d)" % (idx, bus, idx%bus, bus, (-idx)%bus, bus))
    max_modulo *= bus_frequency

print(max_modulo)