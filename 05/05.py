def get_id(repr):
    binstr = repr.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    num = int(binstr, 2)

    return num

passes = [x.strip() for x in open('input.txt', 'r').read().strip().split("\n")]

seats = [get_id(pas) for pas in passes]

seats.sort()

print(seats)
for idx, s in enumerate(seats):
    if idx !=0:
        if seats[idx]-seats[idx-1] == 2:
            print(s)