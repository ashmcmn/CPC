fountains = [1, 2, 1]

n = len(fountains)
ranges = [-1]*n

for i in range(1, len(fountains)+1):
    ranges[i-1] = max(fountains[max(i - fountains[i-1], 1)], min(i + ranges[i-1], n))

c = 1
right = ranges[0]
pointer = 0

for i in range(n):
    pointer = max(pointer, ranges[i])

    if i == right:
        c += 1
        right = pointer

print(c)
