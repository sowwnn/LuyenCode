import math
def giaiPTBac2(a, b, c):
    if (a == 0):
        if (b == 0):
            print("INF")
        else:
            print(format(-c / b,'.2f'))
        return;
    delta = b * b - 4 * a * c;
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print(format(x1,'.2f')+" "+format(x2,'.2f')) if x1<x2 else print(format(x2,'.2f')+" "+format(x1,'.2f'))
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print(format(x1,'.2f'))
    else:
        print("NO")


if __name__ == '__main__':
    a,b,c = [int (x) for x in input().split()]
    giaiPTBac2(a,b,c)

