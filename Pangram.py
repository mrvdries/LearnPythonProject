def readLines(n):
    list = []
    while n!=0:
        s = input()
        list.append(s.lower())
        n-=1
    return list

def testPangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for char in alphabet:
        if char in s:
            count+=1
    return count

n = int(input())
list = readLines(n)
for s in list:
    diff = testPangram(s)
    if diff==0:
        print("De zin is een pangram.")
    else:
        print("De zin telt "+repr(diff)+" verschillende letters.")