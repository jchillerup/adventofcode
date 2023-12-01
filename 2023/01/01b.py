
lines = open('input.txt', 'r').read().split("\n")

def munch(input):
    for idx in range(len(input)):
        if input[idx+0].isdigit(): yield input[idx+0]
        if input[idx:].startswith("one"): yield "1"
        if input[idx:].startswith("two"): yield "2"
        if input[idx:].startswith("three"): yield "3"
        if input[idx:].startswith("four"): yield "4"
        if input[idx:].startswith("five"): yield "5"
        if input[idx:].startswith("six"): yield "6"
        if input[idx:].startswith("seven"): yield "7"
        if input[idx:].startswith("eight"): yield "8"
        if input[idx:].startswith("nine"): yield "9"

calibration_sum = 0
for line in lines:
    digits = list(munch(line))

    # print(digits)
    calibration_sum += int("%s%s" % (digits[0], digits[-1]))

print(calibration_sum)  