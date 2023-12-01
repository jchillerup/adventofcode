
lines = open('input-little.txt', 'r').read().split("\n")

calibration_sum = 0
for line in lines:
    digits = list(filter(lambda x: x.isdigit(), list(line)))

    calibration_sum += int("%s%s" % (digits[0], digits[-1]))

print(calibration_sum)