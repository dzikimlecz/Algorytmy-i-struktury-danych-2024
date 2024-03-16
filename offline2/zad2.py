from zad2testy import runtests

# Jan Pulkowski
# (420313)
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

class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

    def __str__(self):
        return '{' + self.val + '}'


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
    q = Node()
    qtail = q.next = Node(1)
    while q.next:
        q = q.next
        if q.val * 2 < size:
            if heap[q.val * 2] == drop:
                heap[q.val * 2] = nxt
                heapifyMaxUp(heap, q.val * 2, size)
                return
            if heap[q.val * 2] > drop:
                qtail.next = Node(q.val * 2)
                qtail = qtail.next
        if q.val * 2 + 1 < size:
            if heap[q.val * 2 + 1] == drop:
                heap[q.val * 2 + 1] = nxt
                heapifyMaxUp(heap, q.val * 2 + 1, size)
                return
            if heap[q.val * 2 + 1] > drop:
                qtail.next = Node(q.val * 2 + 1)
                qtail = qtail.next



def findMin(heap, drop):
    if heap[1] == drop:
        return 1
    q = Node()
    qtail = q.next = Node(1)
    while q.next:
        q = q.next
        if q.val * 2 < len(heap):
            if heap[q.val * 2] == drop:
                return q.val * 2
            if heap[q.val * 2] < drop:
                qtail.next = Node(q.val * 2)
                qtail = qtail.next
        if q.val * 2 + 1 < len(heap):
            if heap[q.val * 2 + 1] == drop:
                return q.val * 2 + 1
            if heap[q.val * 2 + 1] < drop:
                qtail.next = Node(q.val * 2 + 1)
                qtail = qtail.next
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

def testowanie():
    T =  [7, 9, 1, 5, 8, 6, 2, 12]
    k =  4
    p =  5
    expected = 17
    actual = heapSelect(T, k, p)
    print(expected, actual)

#testowanie()
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
