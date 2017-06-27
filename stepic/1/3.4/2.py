with open('', 'r') as inf:
    s = inf.read()
i = 0
n = len(s)
r = ''
while i < n - 1:
    ch = s[i]
    i += 1
    dg = s[i]
    while i < n - 1:
        if s[i + 1].isdigit():
            i += 1
            dg += s[i]
        else:
            break
    i += 1
    r += ch * int(dg)
print(r)
with open('', 'w') as outf:
    outf.write(r)
