from collections import deque

q = deque( maxlen=5 )
test = False
while True:
    s = input()
    if s.lower() == "stop":
        break
    try:
        f = int(s)
    except ValueError:
        f = float(s)
    if f >= 25:
        if f>=30:
            q.append(0)
        else:
            q.append(1)
        if q.count(1)==3:
            test = True
    else:
        q.clear()
if test:
    print("hittegolf")
else:
    print("geen hittegolf")