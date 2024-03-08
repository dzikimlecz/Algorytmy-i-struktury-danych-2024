from zad1testy import Node, runtests

# Jan Pulkowski
# Numer indeksu: 420313
#
# Sortowanie k-chaotycznej listy n-elementowej.

class QueueNode:
    def __init__(self, leftChild, val=float("inf")):
        self.parent = None
        self.left = None
        self.right = None
        self.leftChild = leftChild
        self.val = val

    def fix(self):
        cursor = self
        while cursor is not None:
            smallest = cursor
            left = cursor.left
            right = cursor.right
            if left is not None and left.val < cursor.val:
                smallest = left
            if right is not None and right.val < smallest.val:
                smallest = right
            if smallest is not cursor:
                smallest.val, cursor.val = cursor.val, smallest.val
                cursor = smallest
            else:
                cursor = None

    def __str__(self):
        return "{" + str(self.val) + "}"


class LinkedQueue:
    def __init__(self, size, sequence):
        self.root = QueueNode(None)
        self.root.val = sequence.val
        self.size = size
        self.fill(sequence.next)
        self.fix()

    def fill(self, sequence):
        i = 1
        tail = queue = Node()
        queue.val = self.root
        while i < self.size and sequence is not None:
            queue.val.left = QueueNode(True, sequence.val)
            queue.val.left.parent = queue.val
            tail.next = Node()
            tail.next.val = queue.val.left
            tail = tail.next
            sequence = sequence.next
            i += 1
            if i < self.size and sequence is not None:
                queue.val.right = QueueNode(False, sequence.val)
                queue.val.right.parent = queue.val
                tail.next = Node()
                tail.next.val = queue.val.right
                tail = tail.next
                sequence = sequence.next
                i += 1
            queue = queue.next

    def fix(self):
        fixi = self.size // 2
        while fixi:
            self.goto(fixi).fix()
            fixi -= 1

    def goto(self, i):
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

    def pop(self, replacement=float("inf")):
        value = self.root.val
        self.root.val = replacement
        self.root.fix()
        return value


def prioritySort(p, k):
    heapSize = k + 1
    q = LinkedQueue(heapSize, p)
    cursor = p
    for _ in range(heapSize):
        if cursor is not None:
            cursor = cursor.next
    head = tail = Node()
    while cursor is not None:
        tail.next = Node()
        tail = tail.next
        tail.val = q.pop(cursor.val)
        cursor = cursor.next
    nextVal = q.pop()
    while nextVal != float("inf"):
        tail.next = Node()
        tail = tail.next
        tail.val = nextVal
        nextVal = q.pop()
    return head.next


def SortH(p,k):
    if k == 0:
        return p
    return prioritySort(p, k)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )


