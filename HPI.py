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
    country = readString("country")
    wealth = readDigit("wealth")
    lifeExp = readDigit("life expectancy")
    footPr = readDigit("foot print")
    hpi = wealth*lifeExp/footPr
    print("De HPI van "+country+" is "+"%0.2f" % hpi +".")
except ValueError as exp:
    print("Error", exp)