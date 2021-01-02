if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=True)

    i = 0
    l = len(arr) - 1

    # Method 1
    while i < l:
        if arr[i] == arr[i + 1]:
            del arr[i+1]
            l -= 1
        else:
            i += 1

    print(arr)
    print(arr[1])

    # Method 2
    print("Method 2")

    lis = list(map(int, input().split()))
    z = max(lis)

    print("List: " + str(lis))

    while max(lis) == z:
        lis.remove(max(lis))

    print(max(lis))
