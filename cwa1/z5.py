#!/usr/bin/env python3

from z2 import Node


def reverse(firstNode: Node) -> Node:
    sent = Node()
    cursor = firstNode
    lastAttached = sent
    while cursor is not None:
        nextNode = cursor.nextNode
        cursor.nextNode = lastAttached
        lastAttached = cursor
        cursor = nextNode
    firstNode.nextNode = None
    return lastAttached


if __name__ == '__main__':
    first = Node()
    first.val = 2
    first.nextNode = Node()
    first.nextNode.val = 1
    first.nextNode.nextNode = Node()
    first.nextNode.nextNode.val = 3
    r = reverse(first)
    while r is not None:
        print(r.val)
        r = r.nextNode
