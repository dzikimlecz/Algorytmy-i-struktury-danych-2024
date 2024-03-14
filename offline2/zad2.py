from zad2testy import runtests

class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

    def __str__(self):
        return '{' + self.val + '}'


def heapifyMin(hp, i, size):
    smallest = i
    left = 2 * i
    right = 2 * i + 1
    if left < size and hp[smallest] > hp[left]:
        smallest = left
    if right < size and hp[smallest] > hp[right]:
        smallest = right
    if smallest != i:
        hp[i], hp[smallest] = hp[smallest], hp[i]
        heapifyMin(hp, smallest, size)


def heapifyMax(hp, i, size):
    largest = i
    left = 2 * i
    right = 2 * i + 1
    if left < size and hp[largest] < hp[left]:
        largest = left
    if right < size and hp[largest] < hp[right]:
        largest = right
    if largest != i:
        hp[i], hp[largest] = hp[largest], hp[i]
        heapifyMax(hp, largest, size)

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
    q = Node()
    qtail = q.next = Node(1)
    while q.next:
        q = q.next
        if heap[q.val] != drop:
            if q.val * 2 < size and heap[q.val * 2] >= drop:
                qtail.next = Node(q.val * 2)
                qtail = qtail.next
            if q.val * 2 + 1 < size and heap[q.val * 2 + 1] >= drop:
                qtail.next = Node(q.val * 2 + 1)
                qtail = qtail.next
        else:
            q.next = None
            heap[q.val] = nxt
            heapifyMaxUp(heap, q.val, size)


def findMin(heap, drop):
    q = Node()
    qtail = q.next = Node(1)
    while q.next:
        q = q.next
        if heap[q.val] != drop:
            if q.val * 2 < len(heap) and heap[q.val * 2] <= drop:
                qtail.next = Node(q.val * 2)
                qtail = qtail.next
            if q.val * 2 + 1 < len(heap) and heap[q.val * 2 + 1] <= drop:
                qtail.next = Node(q.val * 2 + 1)
                qtail = qtail.next
        else:
            return q.val
    return -1




def heapSelect(t, k, p):
    n = len(t)
    minHeap = [0 for _ in range(k + 1)]
    maxHeap = [0 for _ in range(p + 1)]
    minHeap[0] = maxHeap[0] = -1
    for i in range(p):
        maxHeap[i + 1] = t[i]
    buildHeapMax(maxHeap)
    maxSize = p + 1
    for j in range(k):
        pop = maxHeap[1]
        maxHeap[1] = -1
        maxSize -= 1
        heapifyMax(maxHeap, 1, maxSize)
        minHeap[j + 1] = pop
    buildHeapMin(minHeap)
    ssum = minHeap[1]
    for i in range(1, n - p):
        drop = t[i - 1]
        nxt = t[i + p]
        if drop < minHeap[1]:
            replaceMax(maxHeap, maxSize, drop, nxt)
        else:
            ix = findMin(minHeap, drop)
            maxHeap[maxSize] = nxt
            heapifyMaxUp(maxHeap, maxSize, maxSize + 1)
            minHeap[ix] = maxHeap[1]
            heapifyMinUp(minHeap, ix, len(minHeap))
            maxHeap[1] = -1
            heapifyMax(maxHeap, 1, maxSize + 1)
        if minHeap[1] < maxHeap[1]:
            minHeap[1], maxHeap[1] = maxHeap[1], minHeap[1]
        ssum += minHeap[1]
    return ssum



def ksum(T, k, p):
    # tu prosze wpisac wlasna implementacje
    return heapSelect(T, k, p)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=False )
