def sum_digits(n):
    if len(str(n)) != 1:
        return (n % 10) + sum_digits(n // 10)
    else:
        return n


print(sum_digits(234))
