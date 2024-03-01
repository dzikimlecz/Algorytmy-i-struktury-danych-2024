#!/usr/bin/env python3

class Node:
    def __init__(self):
        self.nextNode = None
        self.val = None


def sortList(first: Node):
    sent = Node()
    sortingCursor = sent
    while first is not None:
        mini = first
        miniPrev = None
        cursor = first
        while cursor.nextNode is not None:
            if cursor.nextNode.val < mini.val:
                mini = cursor.nextNode
                miniPrev = cursor
            cursor = cursor.nextNode
        sortingCursor.nextNode = mini
        sortingCursor = sortingCursor.nextNode
        if miniPrev is not None:
            miniPrev.nextNode = mini.nextNode
        else:
            first = mini.nextNode
        mini.nextNode = None
    result = sent.nextNode
    sent.nextNode = None
    return result

if __name__ == '__main__':
    first = Node()
    first.val = 2
    first.nextNode = Node()
    first.nextNode.val = 1
    first.nextNode.nextNode = Node()
    first.nextNode.nextNode.val = 3
    r = sortList(first)
    while r is not None:
        print(r.val)
        r = r.nextNode
