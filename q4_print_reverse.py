def reverse_int(num):
    num = str(num)
    if len(num) == 1:
        return num[0]
    else:
        return num[len(num) - 1] + reverse_int(num[:-1])


print(reverse_int(12345))
