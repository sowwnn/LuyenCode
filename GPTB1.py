if __name__ == '__main__':
    x1, y1, c1, x2, y2,c2 = [int (x) for x in input().split()]
    # print( x1, y1, c1, x2, y2,c2)
    if x1/x2 == y1/y2:
        if x1/x2 == c1/c2:
            print("VOSONGHIEM")
        else:
            print("VONGHIEM")
    else:
        temp = x2/x1
        b = (c1*temp-c2)/(y1*temp - y2)
        a = (c1 - b*y1)/x1

        print(format(a,'.2f'),format(b,'.2f'))

