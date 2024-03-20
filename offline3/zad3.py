from zad3testy import runtests


def cntingGetTemp(points: list, key: int, n: int) -> list:
    temp = [[0] for _ in range(n + 1)]
    for pt in points:
        k = pt[key]
        temp[k][0] += 1
        temp[k].append(pt)
    for i in range(1, len(temp)):
        temp[i][0] += temp[i - 1][0]
    return temp


def countingSortPacking(points: list, key: int, n: int) -> list:
    temp = cntingGetTemp(points, key, n)
    result = []
    for record in temp:
        if len(record) > 1:
            result.append(record[1:])
    return result


def countingSort(points: list, key: int, n: int) -> list:
    temp = cntingGetTemp(points, key, n)
    result = [0] * len(points)
    for i in range(n, -1, -1):
        record = temp[i]
        while len(record) > 1:
            record[0] -= 1
            result[record[0]] = record.pop()
    return result


def radixSort(points: list) -> list:
    n = len(points)
    partSorted = countingSortPacking(points, 1, n)
    for i in range(len(partSorted)):
        partSorted[i] = countingSort(partSorted[i], 0, n)
    return partSorted


def dominance(P):
    groupSorted = radixSort(P)
    maximas = groupSorted[0]
    for i in range(1, len(groupSorted)):
        newMaximas = [e for e in groupSorted[i]]
        maximasCursor = -1
        ll = len(maximas)
        for j in range(len(groupSorted[i])):
            pt = groupSorted[i][j]
            while maximasCursor + 1 < ll and pt[0] >= maximas[maximasCursor + 1][0]:
                maximasCursor += 1
        maximasCursor += 1
        if maximasCursor < ll:
            newMaximas += maximas[maximasCursor:]
        maximas = newMaximas
    maxDom = 0
    for maximum in maximas:
        i = 0
        j = 0
        dom = 0
        while i < len(groupSorted) and maximum[1] > groupSorted[i][j][1]:
            while j < len(groupSorted[i]) and maximum[0] > groupSorted[i][j][0]:
                dom += 1
                j += 1
            j = 0
            i += 1
        maxDom = max(maxDom, dom)
    return maxDom


# zmien all_tests na True zeby uruchomic wszystkie testy

runtests( dominance, all_tests = True )

