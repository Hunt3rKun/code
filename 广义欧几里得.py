def gcd(big, small):
    while small:
        r = big % small
        big = small
        small = r
    return str(big)


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

    print("s= "+str(s[n])+"   t= "+str(t[n]))


a = int(input("输入第一个数a："))
b = int(input("输入第二个数b："))
if a > b:
    big = a
    small = b
else:
    big = b
    small = a

print("a,b的最大公约数为："+gcd(big, small))
ex_gcd(big, small)

