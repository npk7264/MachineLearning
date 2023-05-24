import sys

online_players = set()
result = []

while True:
    inp = sys.stdin.readline().strip()
    if inp:
        if inp[0] == "0":
            break
        a, b = map(int, inp.split(" "))
        if a == 1:
            online_players.add(b)
        elif a == 2:
            if b in online_players:
                result.append(1)
            else:
                result.append(0)
        elif a == 3:
            online_players.discard(b)
        else: break
    else: break

for i in result:
    print(i)