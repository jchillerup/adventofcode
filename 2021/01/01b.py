from itertools import islice

numbers = [int(x) for x in open('input').read().strip().split("\n")]
window_size = 3

incr = 0
old_reading = 0

for i in range(len(numbers) - window_size + 1):
    reading = sum(numbers[i: i + window_size])
    
    if old_reading == 0: 
        old_reading = reading
        continue

    if reading > old_reading:
        incr += 1
    
    old_reading = reading

print(incr)