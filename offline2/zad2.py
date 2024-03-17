from zad2testy import runtests

# Jan Pulkowski
# (420313)
# Złożoność pamięciowa O(p), obliczeniowa O(n * p^2)
# Algorytm:
# Biorę 1. p elementów listy, sortuję je.
# Biorę k-ty największy z nich, dodaję do sumy.
# Dla każdej kolejnej podlisty:
# Binarnie wyszukuję element do usunięcia
# i pozycję do wstawienia nowego elementu,
# tak by podlista dalej była posortowana.
# Biorę k-ty największy element podlisty, dodaję do sumy.
# Po pętli zwracam sumę.


def binSearch(t, val):
    start = 0
    end = len(t) - 1
    while start != end:
        test = (start + end) // 2 + (start + end) % 2
        if t[test] > val:
            end = test - 1
        else:
            start = test
    return start if t[start] == val else None


def posBinSearch(t, val):
    if val <= t[0]:
        return 0
    if t[-1] <= val:
        return len(t)
    start = 1
    end = len(t) - 1
    while start != end:
        test = (start + end) // 2 + (start + end) % 2
        if t[test - 1] > val:
            end = test - 1
        else:
            start = test
    return start if t[start - 1] <= val < t[start] else None


def partition(T, start, end):
    pivot = T[start]
    left = start - 1
    right = end + 1
    while True:
        while True:
            left += 1
            if T[left] >= pivot:
                break
        while True:
            right -= 1
            if T[right] <= pivot:
                break
        if left >= right:
            return right
        T[left], T[right] = T[right], T[left]


def quickSort(T, start, end):
    while start >= 0 and end >= 0 and start < end:
        partIndex = partition(T, start, end)
        quickSort(T, start, partIndex)
        start = partIndex + 1


def ksum(T, k, p):
    n = len(T)
    cp = T[0:p]
    quickSort(cp, 0, p - 1)
    ssum = cp[p - k]
    for i in range(n - p):
        ix = binSearch(cp, T[i])
        del cp[ix]
        new = T[i + p]
        insertIx = posBinSearch(cp, new)
        cp.insert(insertIx, new)
        ssum += cp[p-k]
    return ssum


runtests( ksum, all_tests=True )
