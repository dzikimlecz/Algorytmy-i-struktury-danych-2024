from zad1testy import Node, runtests

# Jan Pulkowski
# Numer indeksu: 420313
#
# Sortowanie k-chaotycznej listy n-elementowej.

INFINITY = float('inf')

class QueueNode:
    def __init__(self, val=INFINITY):
        self.left = None
        self.right = None
        self.val = val

    def fix(self):
        cursor = self
        while cursor is not None:
            smallest = cursor
            left = cursor.left
            right = cursor.right
            if left is not None and left.val.val < cursor.val.val:
                smallest = left
            if right is not None and right.val.val < smallest.val.val:
                smallest = right
            if smallest is not cursor:
                smallest.val, cursor.val = cursor.val, smallest.val
                cursor = smallest
            else:
                cursor = None

    def __str__(self):
        return "{" + str(self.val.val) + "}"


class LinkedQueue:
    def __init__(self, sequence, size):
        self.size = size
        self.root = QueueNode(sequence)
        self.sequence = sequence.next
        self.fill()
        self.fix()

    def fill(self):
        i = 1
        tail = queue = Node()
        queue.val = self.root
        while i < self.size and self.sequence is not None:
            queue.val.left = QueueNode(self.sequence)
            tail.next = Node()
            tail.next.val = queue.val.left
            tail = tail.next
            self.sequence = self.sequence.next
            i += 1
            if i < self.size and self.sequence is not None:
                queue.val.right = QueueNode(self.sequence)
                tail.next = Node()
                tail.next.val = queue.val.right
                tail = tail.next
                self.sequence = self.sequence.next
                i += 1
            queue = queue.next

    def fix(self):
        fixi = self.size // 2
        while fixi:
            self.getNode(fixi).fix()
            fixi -= 1

    def getNode(self, i):
        stack = Node()
        while i > 1:
            new = Node()
            new.next = stack
            new.val = i % 2
            stack = new
            i //= 2
        cursor = self.root
        while stack.val is not None:
            cursor = cursor.right if stack.val else cursor.left
            stack = stack.next
        return cursor

    def poll(self):
        return self.root.val

    def pop(self):
        value = self.root.val
        if self.sequence is not None:
            self.root.val = self.sequence
            self.sequence = self.sequence.next
        else:
            self.root.val = Node()
            self.root.val.val = INFINITY
        self.root.fix()
        return value


def prioritySort(p, k):
    q = LinkedQueue(p, k + 1)
    head = tail = Node()
    nextNode = q.pop()
    while nextNode.val != INFINITY:
        tail.next = nextNode
        tail = tail.next
        tail.next = None
        nextNode = q.pop()
    return head.next

def insert(q, node):
    notFound = True
    while notFound and q.next is not None:
        if node.val < q.next.val:
            node.next = q.next
            notFound = False
        else:
            q = q.next
    q.next = node
    if notFound:
        node.next = None


def insertionSort(p, k):
    queue = Node()
    cursor = p
    i = 0
    while i < k + 1 and cursor is not None:
        inserted = cursor
        cursor = cursor.next
        insert(queue, inserted)
        i += 1
    del i
    head = tail = Node()
    while queue.next is not None:
        tail.next = queue.next
        tail = tail.next
        queue.next = tail.next
        if cursor is not None:
             inserted = cursor
             cursor = cursor.next
             insert(queue, inserted)
        else:
            tail.next = queue.next
    return head.next


def SortH(p,k):
    if k == 0:
        return p
    if k < 9:
        return insertionSort(p, k)
    return prioritySort(p, k)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
