def m_series(i):
    result = (i / (2 * i + 1))
    if i != 1:
        return result + m_series(i - 1)
    else:
        return result


maximum = int(input('Enter number: '))
print("{0:10}m(i)".format("i"))
for a in range(1, maximum + 1):
    print("{0:<10}{1:.4f}".format(a, m_series(a)))
