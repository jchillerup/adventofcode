import re
memory = dict()

p = re.compile("mem\[([0-9]+)\] = ([0-9]+)")

def lsb(s):
    return s[::-1]

def normalize(s):
    return "0"*(36-len(s)) + str(s)

def get_all_addresses(mask):
    if mask.count("X") == 0:
        return [mask]
    buf = ""
    for idx, m in enumerate(mask):
        if m == "0" or m == "1":
            buf += m
        else:
            return [] + get_all_addresses(buf + str("0") + mask[idx+1:]) + get_all_addresses(buf + str("1") + mask[idx+1:])

cur_mask = "X"*36
for line in open('input.txt').readlines():
    line = line.strip()

    if "mask = " in line:
        cur_mask = line[7:]
    else:
        address, value = p.match(line).groups()

        address = "{0:b}".format(int(address))

        # calculate the new address mask:
        new_address_mask = ""
        for m, a in zip(normalize(cur_mask), normalize(address)):
            if m == "0":
                new_address_mask += a
            elif m == "1":
                new_address_mask += "1"
            else:
                new_address_mask += "X"
        
        for new_address in get_all_addresses(new_address_mask):
            memory[int(new_address,2)] = int(value)

sum_ = 0
for key in memory:
    sum_ += memory[key]

print(sum_)