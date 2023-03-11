def base26(w):
    val = 0
    for ch in w.lower():
        next_digit = ord(ch) - ord('a')
        val = 26 * val + next_digit
    return val

print(base26("June"))


