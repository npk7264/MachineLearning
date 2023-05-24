xxx, yy = input().split()
xxx = int(xxx)
yy = int(yy)


def count(xxx, yy):
    cho = (yy-2*xxx)/2
    ga = xxx-cho
    print(int(ga), int(cho))


count(xxx, yy)
