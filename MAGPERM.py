if __name__ == '__main__':
    n,k = [int (x) for x in input().split()]
    arr,b = [],[]
    arr.append(k)
    b.append(k)
    temp = True
    for i in range(1,n+1):
        arr.append(i)
        b.append(i)
    for i in range(1,n):
        b[i],b[i+k] = b[i+k],b[i]
    for i in range(1,n+1):
        if abs(arr[i] - b[i]) != abs(k):
            temp = False
            break
    if(temp or k == 0):
        for i in b[1:]:
            print(i,end=" ")
    else:
        print(-1)