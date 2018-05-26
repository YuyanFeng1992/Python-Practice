def CaseSensitiveHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = []
    for k in range(256):
        skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i+1
        k = k + skip[ord(text[k])]
    return -1


def CaseInsensitiveHorspool(pattern, text):
    pattern = pattern.lower()
    text = text.lower()
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = []
    for k in range(256):
        skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i+1
        k = k + skip[ord(text[k])]
    return -1


def displaymenu():
    print("Welcome to String Search on the Back of Horspool: ")
    print("Case Sensitive,     please input 1")
    print("Case Insensitive,   please input 2")
    print("If you want to quit, please input q")
    i = input("Choose your decision: ")
    return i

def displayall():
    k = []
    i = displaymenu()
    if i == '1':
        f = open('common_test_data_P3.txt', 'r')
        g = open("1.txt", "w")
        lines = f.readlines()
        p = input("The pattern is:")
        for line in lines:
            line = str(line)
            s = CaseSensitiveHorspool(p, line)
            if s > -1:
                g.write(line)
                print(line)
        f.close()
        g.close()
        displayall()
    if i == '2':
        f = open('common_test_data_P3.txt', 'r')
        g = open("1.txt", "w")
        lines = f.readlines()
        p = input("The pattern is:")
        for line in lines:
            line = str(line)
            s = CaseInsensitiveHorspool(p, line)
            if s > -1:
                g.write(line)
                print(line)
        f.close()
        g.close()
        displayall()
    if i == "q":
        exit()
    else:
        print("Invalid input, try again: ")
        displayall()

displayall()
