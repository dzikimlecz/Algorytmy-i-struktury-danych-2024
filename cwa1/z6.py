#!/usr/bin/env python3

# Wyszukuje binarnie 1. danej pozycji
# (1) Jeżeli element na indeksie test jest większy od test
# oraz poprzedni element nie spełnia tego warunku, bądź nie istnieje
# to test jest poszukiwanym indeksem
# jeżeli A[test] jest równe test to należy przeszukać dalszą część tablicy
# jeżeli A[test] jest większe od test ale poprzedni element istnieje i również spełnia ten warunek
# (co wiadomo z 1. części tej koniunkcji gdyż inaczej wyczerpał by warunek (1))
# to należy przeszukać część tablicy przed indeksem test
# jeżeli żaden z powyższych warunków nie jest spełniony
# to dane są błędne
def solve(A):
    start = 0
    end = len(A)
    while start != end:
        test = (start + end) // 2
        if A[test] > test and (test == 0 or A[test - 1] == test - 1):
            start = end = test
        elif A[test] == test:
            start = test + 1
        elif A[test] > test:
            end = test
        else:
            print("błąd danych")
            return -1
    if test == A[test]:
        print("błąd danych")
        return -1
    return test


if __name__ == '__main__':
   t = [0, 1, 2, 4, 5, 6]
   print(solve(t))
