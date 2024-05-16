#!/usr/bin/env python3

# Jan Pulkowski
# (420313)
#
# Dijkstra O(V^2)
# Złożoność pamięciowa: O(E + V)

from queue import PriorityQueue
from zad6testy import runtests

BOOTS_JUMP = 0
BOOTS = 1
NO_BOOTS = 2

def jumper(g,s,w):
    return findWay(g, s, w)

def findWay(graph, start, end):
    v = len(graph)
    distances = [[float('inf'), float('inf')] for _ in range(v)]
    distances[start][0] = distances[start][1] = 0
    q = PriorityQueue()
    q.put((0, BOOTS, 0, start))
    while not q.empty():
        #breakpoint()
        d, boots, previousEdgeLen, node = q.get()
        if node == end and boots != BOOTS_JUMP:
            break
        for i in range(v):
            if graph[node][i]:
                edge = graph[node][i]
                if boots == BOOTS_JUMP:
                    newD = d + max(previousEdgeLen, edge)
                    if newD < distances[i][1]:
                        q.put((newD, NO_BOOTS, edge, i))
                        distances[i][1] = newD
                else:
                    newD = d + edge
                    if boots == BOOTS:
                        q.put((d, BOOTS_JUMP, edge, i))
                    if newD < distances[i][0]:
                        q.put((newD, BOOTS, edge, i))
                        distances[i][0] = newD
    d = min(distances[end][0], distances[end][1])
    return d if d != float('inf') else None


runtests( jumper, all_tests = True )

def testuj():
    S=[[0, 1, 200, 200, 200, 200], [1, 0, 2, 200, 200, 200], [200, 2, 0, 40, 200, 200], [200, 200, 40, 0, 40, 200], [200, 200, 200, 40, 0, 117], [200, 200, 200, 200, 117, 0]]
    s=0
    w=4
    print(jumper(S, s, w))

#testuj()
