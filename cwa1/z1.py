#!/usr/bin/env python3

def posortuj(lista: list):
    sortedCursor = 0
    size = len(lista)
    while sortedCursor < size:
        el = lista[sortedCursor]
        cursor = 0
        while cursor < sortedCursor and not (lista[cursor] <= el < lista[cursor + 1]):
            cursor += 1
        if cursor != sortedCursor:
            insertionPoint = cursor + 1
            print("moving", el, "from", sortedCursor, "to", insertionPoint)
            for moveCursor in range(sortedCursor, insertionPoint, -1):
                lista[moveCursor] = lista[moveCursor - 1]
            if insertionPoint < size:
                lista[insertionPoint] = el
            print(lista)
        sortedCursor += 1


def main():
    l = [0, 7, 2137, 3, 0, 5]
    print(l)
    posortuj(l)
    print(l)


if __name__ == '__main__':
    main()
