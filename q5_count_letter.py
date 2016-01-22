def count_letter(string, ch):
    if string[len(string) - 1] == ch:
        if len(string) == 1:
            return 1
        return 1 + count_letter(string[:-1], ch)
    else:
        if len(string) != 1:
            return count_letter(string[:-1], ch)
        else:
            return 0


print(count_letter("Welcome", "e"))
