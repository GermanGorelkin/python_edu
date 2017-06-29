total_var1 = 0.0
total_var2 = 0.0
total_var3 = 0.0
cnt = 0

with open('', 'r') as inf:
    for i in inf:
        s = i.split(';')
        var1 = float(s[1])
        var2 = float(s[2])
        var3 = float(s[3])
        total_var1 += var1
        total_var2 += var2
        total_var3 += var3
        cnt += 1
        print((var1 + var2 + var3) / 3)
print(total_var1/cnt, total_var2/cnt, total_var3/cnt)
