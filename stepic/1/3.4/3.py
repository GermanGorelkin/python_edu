with open('', 'r') as inf:
    l = [i.lower() for i in inf.read().split(' ')]
d = {}
max_key = ''
max_value = 0
for item in l:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
    if d[item] > max_value:
        max_value = d[item]
        max_key = item

print(max_key, max_value)
