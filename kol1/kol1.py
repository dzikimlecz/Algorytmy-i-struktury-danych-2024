from kol1testy import runtests

# Jan Pulkowski
# 420313
#
#
# Oczekiwane O(nlogn)
# 1. Posortuj malejąco indeksy tablicy.
# 2. Jeżeli element powinien się znaleść na indeksie i a jest na indkesie j : j > i, to
#    znaczy że jest przed nim co najmiej j - i elementów nie większych od niego
# 3. Jeżeli jest więcej niż j - i elementów nie większych od niego to znaczy, że
#    któryś z elementów większych od niego znajduje się za nim więc będzie miał on większą rangę
# 4. Stąd, liderowi przyporządkuje się w ten sposób dokładną liczbę elementów które są przed nim
#    i nie są od niego większe
# 5. Następnie należy ustalić ile jest elementów któ©e są mu równe i są przed nim



def maxrank(T):
    n = len(T)
    sortedIndices = qsort(T)
    maxDiff = -1
    for i in range(n):
        diff = sortedIndices[i] - i
        if diff > maxDiff:
            j = i + 1
            while j < n and T[sortedIndices[i]] == T[sortedIndices[j]] and sortedIndices[j] < sortedIndices[i]:
                diff -= 1
                j += 1
            # print(j - i)
            maxDiff = max(maxDiff, diff)
    return maxDiff



def qsort(t) -> list:
    n = len(t)
    indices = [i for i in range(n)]
    quickSort(t, indices, 0, n - 1)
    return indices


def quickSort(values, indices, start, end):
    while start >= 0 and end >= 0 and start < end:
        partIndex = partition(values, indices, start, end)
        quickSort(values, indices, start, partIndex)
        start = partIndex + 1


def partition(values, indices, start, end):
    pivot = values[indices[start]]
    left = start - 1
    right = end + 1
    while True:
        while True:
            left += 1
            if values[indices[left]] <= pivot:
                break
        while True:
            right -= 1
            if values[indices[right]] >= pivot:
                break
        if left >= right:
            return right
        indices[left], indices[right] = indices[right], indices[left]


#t = [1,2,3]
#print(binSearch(t, qsort(t), 3))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
