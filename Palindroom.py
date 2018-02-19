def invCompliment(s):
    s = s.lower()
    new_s = ''
    for char in s:
        if char == 'c':
            char = 'g'
        elif char == 'g':
            char = 'c'
        elif char == 'a':
            char = 't'
        elif char == 't':
            char = 'a'
        else:
            raise AssertionError("string bevat foutief character", char)
        new_s = char + new_s
    return new_s

def DNAPalindroom(s):
    if s == invCompliment(s):
        return True
    return False

