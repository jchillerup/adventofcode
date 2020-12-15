import re
memory = dict()

p = re.compile("mem\[([0-9]+)\] = ([0-9]+)")

def lsb(s):
    return s[::-1]

def normalize(s):
    return "0"*(36-len(s)) + str(s)


cur_mask = "X"*36
for line in open('input.txt').readlines():
    line = line.strip()

    if "mask = " in line:
        cur_mask = line[7:]
    else:
        address, value = p.match(line).groups()

        value = "{0:b}".format(int(value))

        new_value = ""
        for m, v in zip(normalize(cur_mask), normalize(value)):
            if m == "0":
                new_value += "0"
            elif m == "1":
                new_value += "1"
            else:
                new_value += v
        
        memory[address] = int(new_value, 2)

sum_ = 0
for key in memory:
    sum_ += memory[key]

print(sum_)