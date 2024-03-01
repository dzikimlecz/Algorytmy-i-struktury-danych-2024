#!/usr/bin/env python3

def find(arr: list, x):
    size = len(arr)
    start = 0
    end = size
    while start != end:
        test = (start + end) // 2
        if arr[test] == x:
            start = end = test
        elif arr[test] > x:
            end = test
        else:
            start = test + 1
    if arr[start] == x:
        return start
    else:
        return -1

if __name__ == '__main__':
    a = [1, 4, 5, 6, 9]
    print(find(a, 7))
