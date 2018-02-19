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
    country = readString("country")
    wealth = readDigit("wealth")
    lifeExp = readDigit("life expectancy")
    footPr = readDigit("foot print")
    hpi = wealth*lifeExp/footPr
    print("De HPI van "+country+" is "+"%0.2f" % hpi +".")
except ValueError as exp:
    print("Error", exp)