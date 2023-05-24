n = int(input())
k = int(input())
p = int(input())
q = int(input())


def getPosition(n, k, p, q):
    index = p * 2 + q - 2
    position1 = index - k
    position2 = index + k
    row = -1
    col = -1

    next = 1
    if q == 1:
        next = 2

    # print("next", next)

    if p == int((n+1)/2) and q == 2 and n % 2 != 0:
        print(-1)
        return

    ##########################################
    if position1 > 0:
        # print("case1:", "position", position1, "k", k)
        if position1 % 2 == 0:
            row = int(position1 / 2)
        else:
            row = int(position1 / 2) + 1

        if k % 2 == 0:
            col = q
        else:
            col = next
        print(row, col)
        return
    ##########################################
    elif position2 <= n:
        # print("case2", "position", position2, "k", k)
        if position2 % 2 == 0:
            row = int(position2 / 2)
        else:
            row = int(position2 / 2) + 1

        if k % 2 == 0:
            col = q
        else:
            col = next
        if row == int((n+1)/2) and n % 2 != 0 and col == 2:
            print(-1)
            return
        else:
            print(row, col)
            return
    ##########################################
    elif position1 < 1 and position2 > n:
        print(-1)


getPosition(n, k, p, q)
