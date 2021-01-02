if __name__ == '__main__':
    n = int(input())
    ori = list(map(int, input().split()))

    print("Method 1")

    arr = sorted(ori, reverse=True)
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
    print("\nMethod 2")

    lis = ori.copy()
    print(id(lis), id(ori))
    z = max(lis)

    while max(lis) == z:
        lis.remove(max(lis))

    print("List: " + str(lis))
    print(max(lis))

    print("\nMethod 3 (using set)")
    print(set(ori))
    usingset = sorted(list(set(ori)), reverse=True)
    print(usingset)
    print(usingset[1])
