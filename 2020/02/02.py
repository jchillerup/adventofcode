import re

pattern = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

num_good_type_a = 0
num_good_type_b = 0
for password in [x.rstrip() for x in open('input.txt', 'r').read().split("\n")]:
    if password == "": continue

    match = pattern.match(password)
    min_bound, max_bound, needle, haystack = match.groups()

    min_bound = int(min_bound)
    max_bound = int(max_bound)

    print(haystack)

    num_needle = haystack.count(needle)
    if num_needle >= min_bound and num_needle <= max_bound:
        num_good_type_a += 1
    
    num_good_type_b += (haystack[min_bound-1] == needle)^(haystack[max_bound-1] == needle)

print(num_good_type_a)
print(num_good_type_b)