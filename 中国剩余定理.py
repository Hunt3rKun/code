def ex_gcd(a, b):
    s = [0, 1, 0]
    t = [0, 0, 1]
    r = [a, b]
    r.append(r[0] % r[1])
    q = [0, 0, r[0] // r[1]]

    n = 3
    while 1:
        q.append(r[n - 2] // r[n - 1])
        r.append(r[n - 2] % r[n - 1])
        s.append(s[n - 2] - (q[n - 1] * s[n - 1]))
        t.append(t[n - 2] - (q[n - 1] * t[n - 1]))
        if r[n] == 0:
            break
        n = n + 1

    return s[n]


n = int(input('请输入一共有几组同余式： '))
a = []
m = []
M = 1

for i in range(n):
    a.append(int(input('请输入第i个a: ')))
    m.append(int(input('请输入第i个m: ')))
    M = M * m[i]

b = []
cum = 0

for i in range(n):
    b.append(M / m[i])
    b[i] = b[i] * ex_gcd(b[i], m[i]) * a[i]
    cum = cum + b[i]

print("最后的解是： "+str(int(cum % M)))

