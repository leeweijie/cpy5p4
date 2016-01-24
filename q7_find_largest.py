def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    elif alist[len(alist) - 1] < alist[len(alist) - 2]:
        alist.pop(len(alist) - 1)
        return find_largest(alist)
    else:
        alist.pop(len(alist) - 2)
        return find_largest(alist)


print(find_largest([5, 1, 8, 7, 2]))
