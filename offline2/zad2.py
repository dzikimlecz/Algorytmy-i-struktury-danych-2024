from zad2testy import runtests


class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

    def __str__(self):
        return '{' + self.val + '}'


def part(thelist, start, end):
    pivot = thelist[end - 1]
    smallerPartEnd = start
    for i in range(start, end):
        if thelist[i] < pivot:
            thelist[i], thelist[smallerPartEnd] = thelist[smallerPartEnd], thelist[i]
            smallerPartEnd += 1
    thelist[end - 1], thelist[smallerPartEnd] = thelist[smallerPartEnd], thelist[end - 1]
    return smallerPartEnd


def quickSelect(thelist, k):
    stack = Node((0, len(thelist)))
    while stack.val:
        start, end = stack.val
        stack = stack.next
        size = end - start
        pivotIndex = part(thelist, start, end)
        if len(thelist) - k == pivotIndex:
            new = Node()
        elif len(thelist) - k < pivotIndex:
            new = Node((start, pivotIndex))
        else:
            new = Node((pivotIndex + 1, end))
        new.next = stack
        stack = new
    return thelist[pivotIndex]


def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    ssum = 0
    n = len(T)
    for i in range(0, n - p + 1):
        sub = T[i : i + p]
        ssum += quickSelect(sub, k)
    return ssum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
