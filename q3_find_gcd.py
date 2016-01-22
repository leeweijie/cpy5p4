def gcd(m, n):
    d = min(m, n)
    if m % d == 0 and n % d == 0:
        if n != 1:
            return n
        else:
            return 1
    else:
        gcd(m, n - 1)


print(gcd(90, 45))
