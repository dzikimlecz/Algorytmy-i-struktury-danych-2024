from zad4testy import runtests
from collections import deque
# Jan Pulkowski
#   (420313)
# Złożoność O(E(V+E))
# Algorytm Gąsienicowo przeszukuje posortowaną listę krawędzi
# szukając ścieżki spełniającej parametry zadania

DEBUG = False

def Flight(L,x,y,t):
    L = sorted(L, key=lambda x: x[2])
    l = len(L)
    q = deque()
    v = 0
    for i in range(l):
        v = max((v, L[i][0], L[i][1]))
    v += 1
    if x >= v or y >= v:
        return False
    graph = [[] for _ in range(v) ]
    ibuff = [ 0 for _ in range(v) ]
    j = -1
    i = 0
    found = False
    while not found and i < l and j < l:
        moved = False
        while j + 1 < l and abs(L[j + 1][2] - L[i][2]) <= 2 * t:
            j += 1
            moved = True
            graph[L[j][0]].append(L[j][1])
            graph[L[j][1]].append(L[j][0])
        if moved:
            endsIn = len(graph[x]) - ibuff[x]
            endsIn = endsIn and len(graph[y]) - ibuff[y]
            if endsIn:
                q.clear()
                found = lookForPath(q, graph, x, y, ibuff)
        ibuff[L[i][0]] += 1
        ibuff[L[i][1]] += 1
        i += 1
    return found


def lookForPath(q: deque, graph, x, y, ibuff):
    v = len(graph)
    visited = [False] * v
    visited[x] = True
    q.append(x)
    found = False
    while len(q) and not found:
        node = q.popleft()
        if node == y:
            found = True
        else:
            for i in range(ibuff[node], len(graph[node])):
                e = graph[node][i]
                if not visited[e]:
                    q.append(e)
                    visited[e] = True
    return found



# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( Flight, all_tests = True )
L = input()
L = eval(L)
x = int(input())
y = int(input())
t = int(input())
print(Flight(L, x, y, t))
