ans = 0
temp_set = []
for obj in objects:
    if obj not in temp_set:
        temp_set.append(obj)
        ans += 1

print(ans)