from zad4testy import runtests

# Jan Pulkowski
#   (420313)
# Złożoność O(n!)
# Backtracking

DEBUG = False

class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.size = 0

    def peek(self):
        return self.data[self.size - 1] if self.size > 0 else None

    def pop(self):
        result = None
        if self.size > 0:
            self.size -= 1
            result = self.data[self.size]
        return result

    def push(self, val):
        l = len(self.data)
        if self.size == l:
            newData = [self.data[i] if i < l else None for i in range(2 * l)]
            self.data = newData
            l = len(self.data)
        self.data[self.size] = val
        self.size += 1

    def empty(self) -> bool:
        return self.size == 0

    def notEmpty(self) -> bool:
        return self.size > 0

def Flight(L,x,y,t):
    g = makeGraph(L)
    return check(g, x, y, 2 * t, len(L))


def makeGraph(l: list) -> list:
    v = 0
    for i in range(len(l)):
        v = max((v, l[i][0], l[i][1]))
    graph = [[] for _ in range(v + 1)]
    for edge in l:
        v1, v2, h = edge
        graph[v1].append((v2, h))
        graph[v2].append((v1, h))
    return graph

def check(graph: list, start: int, dest: int, heightAmp: int, sSize: int) -> bool:
    v = len(graph)
    stack = Stack(sSize)
    visited = [False] * v
    stack.push((start, float('inf'), 0, True))
    found = False
    while not found and stack.notEmpty():
        record = stack.pop()
        elem = record[0]
        if not record[3]:
           visited[elem] = False
        else:
            visited[elem] = True
            if elem == dest:
                found = True
            else:
                stack.push((elem, record[1], record[2], False))
                for child in graph[elem]:
                    if not visited[child[0]]:
                        minh, maxh = min(record[1], child[1]), max(record[2], child[1])
                        if maxh - minh <= heightAmp:
                            stack.push((child[0], minh, maxh, True))

    return found




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
#L = [(0,1,1606),(0,3,612),(0,4,549),(0,8,909),(1,4,442),(2,3,1020),(2,5,465),(2,6,1598),(3,5,1667),(4,8,1096),(5,10,993),(6,11,1501),(7,9,1050),(9,10,1762),(11,12,1900),(11,13,717)]
#x = 2
#y = 9
#t = 522
#print(Flight(L, x, y, t))
