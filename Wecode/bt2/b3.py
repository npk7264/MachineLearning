from sys import stdin
lst = []

while True:
    i = stdin.readline().strip().split(" ")

    if i[0] == "6":
        break
    if i[0] == "0":
        lst.insert(0, i[1])
    elif i[0] == "1":
        lst.append(i[1])
    elif i[0] == "2":
        try:
            pos = int(lst.index(i[1])) + 1
            lst.insert(pos, i[2])
        except:
            lst.insert(0, i[2])
    elif i[0] == "3":
        try:
            lst.remove(i[1])
        except:
            pass
    elif i[0] == "4":
        try:
            while True:
                lst.remove(i[1])
        except:
            pass
    elif i[0] == "5":
        try:
            lst.pop(0)
        except:
            pass
    else:
        break

if len(lst) != 0:
    print(*lst)
else:
    print("blank")
