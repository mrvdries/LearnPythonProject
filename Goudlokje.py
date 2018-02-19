def readString(s):
    s = input(s+": ")
    return s
def readDigit(s):
    s = input(s+": ")
    try:
        f = int(s)
    except ValueError:
        f = float(s)
    return f

try:
    val = readDigit("value")
    min = readDigit("minimum")
    max = readDigit("maximum")
    minatt = readString("minimum attribute")
    maxatt = readString("maximum attribute")
    if val < min:
        result = "te "+minatt
    elif val > max:
        result = "te " + maxatt
    else:
        result = "juist goed"

    print(result)
except ValueError as exp:
    print("Error", exp)