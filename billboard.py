def printSets(set1, set2):
    print(sum(set1))


def findSets(arr, n, set1, set2, sum1, sum2, pos):

    if (pos == n):

        if (sum1 == sum2):
            printSets(set1, set2)
            return True

        else:
            return False

    set1.append(arr[pos])

    res = findSets(arr, n, set1, set2,
                   sum1 + arr[pos], sum2, pos + 1)

    if (res):
        return res

    set1.pop()
    set2.append(arr[pos])

    res = findSets(arr, n, set1, set2, sum1,
                   sum2 + arr[pos], pos + 1)
    if not res:
        set2.pop()
    return res


def isPartitionPoss(arr, n):

    sum = 0

    for i in range(0, n):
        sum += arr[i]

    if (sum % 2 != 0):
        return False

    set1 = []
    set2 = []

    return findSets(arr, n, set1, set2, 0, 0, 0)


n = int(input())
arr = list(map(int, input().split()))

if (isPartitionPoss(arr, n) == False):
    print(0)
