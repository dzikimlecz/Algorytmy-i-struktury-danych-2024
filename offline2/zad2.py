from zad2testy import runtests


def part(thelist, start, end):
    pivot = thelist[end - 1]
    smallerPartEnd = start
    for i in range(start, end):
        if thelist[i] < pivot:
            thelist[i], thelist[smallerPartEnd] = thelist[smallerPartEnd], thelist[i]
            smallerPartEnd += 1
    thelist[end - 1], thelist[smallerPartEnd] = thelist[smallerPartEnd], thelist[end - 1]
    return smallerPartEnd



def quickSort(thelist, start=0, end=None):
    if end is None:
        end = len(thelist)
    if start < end:
        partIndex = part(thelist, start, end)
        quickSort(thelist, start=start, end=partIndex)
        quickSort(thelist, start=partIndex+1, end=end)



def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    ssum = 0
    n = len(T)
    for i in range(0, n - p + 1):
        sub = T[i : i + p]
        quickSort(sub)
        ssum += sub[len(sub) - k]
    return ssum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
