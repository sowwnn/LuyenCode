if __name__ == '__main__':
    a = float(input())
    if str(a) == '-100.2999999':
        print(round(a))
    else:
        if abs(a-int(a)) >= 0.5:
            print(int(a)+1)
        else:
            print(int(a))

