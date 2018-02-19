def readString(a):
    s = input(a+": ")
    return s
def readDigit(a):
    s = input(a+": ")
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