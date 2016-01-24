def find_num_uppercase(str):
    if str[len(str) - 1].isupper():
        if len(str) == 1:
            return 1
        else:
            return 1 + find_num_uppercase(str[:-1])
    else:
        if len(str) == 1:
            return 1
        else:
            return find_num_uppercase(str[:-1])


print(find_num_uppercase("Good MorninG"))
