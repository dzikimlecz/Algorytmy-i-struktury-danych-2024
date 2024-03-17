from zad2testy import runtests

# Jan Pulkowski
# (420313)
# Złożoność pamięciowa O(p+k), obliceniowa O(np)
# Algorytm Selekcji k-tych największych elementów z użyciem kopców.
# W pamięci przechowywane są 2 kopce, jeden sortujący rosnąco (kopiecMax), drugi malejąco(kopiecMin).
# Początkowo do kopcaMax wczytywane jest p 1. elemenmtów listy,
# następnie k pierwszych elementów kopcaMax jest zdejmowane na kopiecMin.
# 1. element kopcamin to pierwsza k-ta największa wartość - dodaję ją do całościowej sumy.
# Następnie dla pozostałych (p - 1) przedziałów
# usuwam element bespośrednio za przedziałem z kopca w którym się znajdował,
# a na jego miejsce wstawiam element końcowy nowego przedziału.
# Odbudowuję kopce i ewentualnie zamieniam 1. elementy kopcaMin i kopcaMax
# jeżeli ten z kopcaMax jest większy. Uruchamiam na obu procedurę heapify.
# Szczyt kopca min ponownie zawiera k-ty największy element, dodaję go do sumy.


def heapifyMin(hp, i, size):
    while 2 * i < size:
        smallest = i
        left = 2 * i
        right = 2 * i + 1
        if hp[smallest] > hp[left]:
            smallest = left
        if right < size and hp[smallest] > hp[right]:
            smallest = right
        if smallest != i:
            hp[i], hp[smallest] = hp[smallest], hp[i]
            i = smallest
        else:
            i = size


def heapifyMax(hp, i, size):
    while 2 * i < size:
        largest = i
        left = 2 * i
        right = 2 * i + 1
        if hp[largest] < hp[left]:
            largest = left
        if right < size and hp[largest] < hp[right]:
            largest = right
        if largest != i:
            hp[i], hp[largest] = hp[largest], hp[i]
            i = largest
        else:
            i = size


def heapifyMaxUp(heap, i, size):
    while i:
        heapifyMax(heap, i, size)
        i //= 2

def heapifyMinUp(heap, i, size):
    while i:
        heapifyMin(heap, i, size)
        i //= 2


def buildHeapMin(heap):
    size = len(heap)
    for i in range(size // 2, 0 , -1):
        heapifyMin(heap, i, size)


def buildHeapMax(heap):
    size = len(heap)
    for i in range(size // 2, 0, -1):
        heapifyMax(heap, i, size)


def replaceMax(heap, size, drop, nxt):
    if heap[1] == drop:
        heap[1] = nxt
        heapifyMax(heap, 1, size)
        return
    q = [0] * (size)
    qSize = 1
    qStart = 0
    q[0] = 1
    while qSize:
        val = q[qStart]
        qStart += 1
        qSize -= 1
        test = val * 2
        for i in range(2):
            if test < size:
                if heap[test] == drop:
                    heap[test] = nxt
                    heapifyMaxUp(heap, test, size)
                    return
                if heap[test] > drop:
                    q[qStart + qSize] = test
                    qSize += 1
            test += 1


def findMin(heap, drop):
    if heap[1] == drop:
        return 1
    q = [0] * (len(heap))
    qSize = 1
    qStart = 0
    q[0] = 1
    while qSize:
        val = q[qStart]
        qStart += 1
        qSize -= 1
        test = val * 2
        for i in range(2):
            if test < len(heap):
                if heap[test] == drop:
                    return test
                if heap[test] < drop:
                    q[qStart + qSize] = test
                    qSize += 1
            test += 1
    return -1




def heapSelect(t, k, p):
    n = len(t)
    minHeap = [0 for _ in range(k + 1)]
    maxHeap = [0 for _ in range(p + 1)]
    minHeap[0] = maxHeap[0] = None
    for i in range(p):
        maxHeap[i + 1] = t[i]
    buildHeapMax(maxHeap)
    maxSize = p + 1
    for j in range(k):
        pop = maxHeap[1]
        maxHeap[1] = maxHeap[maxSize - 1]
        maxSize -= 1
        heapifyMax(maxHeap, 1, maxSize)
        minHeap[j + 1] = pop
    buildHeapMin(minHeap)
    ssum = minHeap[1]
    for i in range(n - p):
        drop = t[i]
        nxt = t[i + p]
        if drop < minHeap[1]:
            replaceMax(maxHeap, maxSize, drop, nxt)
        else:
            ix = findMin(minHeap, drop)
            maxHeap[maxSize] = nxt
            heapifyMaxUp(maxHeap, maxSize, maxSize + 1)
            minHeap[ix] = maxHeap[1]
            heapifyMinUp(minHeap, ix, len(minHeap))
            maxHeap[1] = maxHeap[maxSize]
            heapifyMax(maxHeap, 1, maxSize)
        if minHeap[1] < maxHeap[1]:
            minHeap[1], maxHeap[1] = maxHeap[1], minHeap[1]
            heapifyMin(minHeap, 1, len(minHeap))
            heapifyMax(maxHeap, 1, maxSize)
        ssum += minHeap[1]
    return ssum

def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    return heapSelect(T, k, p)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
