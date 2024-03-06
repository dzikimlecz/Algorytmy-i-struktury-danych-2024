from zad1testy import Node, runtests

# Jan Pulkowski
# Numer indeksu: 420313
#
# Sortowanie k-chaotycznej listy n-elementowej.
# Jeźeli k == 0, zwracany jest wskaźnik podany przez argument p (lista od początku posortowana).
# Jeżeli 0 < k sortowanie odbywa się ulepszoną wersją sortowania przez wybór (patrz poniżej).
#
#
# Ulepszone sortowanie przez wybór:
# 0. Utwórz pustą posortowaną listę z wartownikiem.
# 1. Wybierz najmniejszy spośród pierwszych (k + 1) elementów nieposortowanej listy.
# 2. Przenieś ten element na koniec posortowanej listy.
# 3. Powtarzaj 1, 2 dopóki nieposortowana lista jest niepusta.
# 4. Usuń wartownika z posortowanej listy, zwróć referencję na 1. element.
#
# ZŁOŻONOŚC OBLICZENIOWA:
# k = THETA(1) => O(1)
# k = THETA(log(n)) => O(n * k)
# k = THETA(n) => O(n * k)
#
# UZASADNIENIE POPRAWNOŚCI ULEPSZONEGO SORTOWANIA PRZEZ WYBÓR:
# Lemat 1: x - najmniejszy element listy, jest jednym z (k + 1) pierwszych elementów listy.
# Dowód:
#   Przypuszczam fałszywość Lematu 1, wówczas odległość x od rządanej pozycji wynosi (index(x) - 0) > k,
#   co jest sprzeczne ze specyfikacją zadania, zatem Lemat 1 jest prawdziwy.
# Lemat 2: Usunięcie z listy najmniejszego elementu nie zwiększy jej chaotyczności.
# Dowód:
#   Niech k będzie chaotycznością danej listy.
#   Wiadomo, że najmniejszy element jest na pozycji m z {0, 1, 2, ..., k}.
#   Niech będzie x - dowolny nienajmniejszy element listy.
#   Niech i oznacza indeks x w liście, a j indeks x w liście posortowanej. Wiadomo, że |i - j| <= k oraz i != m.
#   Niech i', j' oznaczają to samo co odpowiednio i, j, ale po usunięciu najmniejszego elementu z listy.
#   Wiadomo, że x nie jest najmniejszym elementem, stąd j' = j - 1
#   Jeżeli m < i:
#       i' = i - 1
#       |i ' - j'| = |i - j| <= k
#       Chaotyczność listy nie zwiększyła się.
#   Jeżeli i < m.
#       i' = i
#       |i' - j'| = |i - (j - 1)| = j - i - 1 < j - i = |i - j| <= k
#       |i' - j'| <= k
#       Chaotyczność listy nie zwiększyła się.
#   i != m, zatem w każdym przypadku chaotyczność listy nie zwiększyła się, co kończy dowód.
# Z lematu 2, chaotyczność listy w trakcie trwania algorytmu nie wzrośnie;
# z lematu 1 i 2, najmniejszy jeszcze nie usunięty element listy zawsze będzie jednym z (k + 1) elementów listy.
# stąd algorytm jest poprawny.

def enhancedSelectSort(p: Node, k: int) -> Node:
    # Utwórz pustą posortowaną listę z wartownikiem.
    sentinel = Node()
    tail = sentinel
    head = p
    # Powtarzaj 1, 2 dopóki nieposortowana lista jest niepusta.
    while head is not None:
        # 1. Wybierz najmniejszy spośród pierwszych (k + 1) elementów nieposortowanej listy.
        minimalCursor = head
        minimalPrecursor = None
        precursor = head
        cursor = head.next
        i = 0
        while i < k and cursor is not None:
            if cursor.val < minimalCursor.val:
                minimalPrecursor, minimalCursor = precursor, cursor
            precursor, cursor = cursor, cursor.next
            i += 1
        # 2. Przenieś ten element na koniec posortowanej listy.
        if minimalPrecursor is not None:
            minimalPrecursor.next = minimalCursor.next
        else:
            head = head.next
        minimalCursor.next = None
        tail.next = minimalCursor
        tail = tail.next
    # Usuń wartownika z posortowanej listy, zwróć referencję na 1. element.
    head = sentinel.next
    sentinel.next = None
    return head


def SortH(p,k):
    if k == 0:
        return p
    return enhancedSelectSort(p, k)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
