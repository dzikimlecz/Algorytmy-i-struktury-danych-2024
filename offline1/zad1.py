from zad1testy import Node, runtests

# Jan Pulkowski
# Numer indeksu: 420313
#
# Sortowanie k-chaotycznej listy n-elementowej.
#
# ZŁOŻONOŚĆ OBLICZENIOWA
# O(n), dla k = Θ(1)
# O(nlogn), dla k = Θ(log n)
# O(nlogn), dla k = Θ(n)
#
# Dla k <= log_2(n)
# Algorytm realizuje sortowanie poprzez zbudowanie kolejki priorytetowej z k + 1 kolejnych elementów listy od jej początku.
# Następnie elementy kolejki są z niej w odpowiedniej kolejności zdejmowane i łączone w posortowaną listę.
# Kolejka jest realizowana poprzez sortowanie przez wstawianie listy jednokrotnie powiązanej.
#
# Dla k > log_2(n)
# Sortowanie odbywa się przez scalanie.
#
# UZASADNIENIE POPRAWNOŚCI:
# Lemat: x - najmniejszy element listy, jest jednym z (k + 1) pierwszych elementów listy.
# Dowód:
#   Przypuszczam fałszywość Lematu 1, wówczas odległość x od rządanej pozycji wynosi (index(x) - 0) > k,
#   co jest sprzeczne ze specyfikacją zadania, zatem Lemat 1 jest prawdziwy.
# Przez indukcję matematyczną można udowodnić z lematu, że kolejne wybieranie ze zbioru k + 1 elementów listy najmniejszego
# a następnie dodawanie kolejnego elementu listy da ciąg jej posortowanych elementów.

def selectSort(p, k):
    queue = Node()
    cursor = p
    i = 0
    # Wypełnai kolejkę pierwszymi k + 1 elementami
    while i < k + 1 and cursor is not None:
        node = cursor
        cursor = cursor.next
        notFound = True
        q = queue
        while notFound and q.next is not None:
            if node.val < q.next.val:
                node.next = q.next
                notFound = False
            else:
                q = q.next
        q.next = node
        if notFound:
            node.next = None
        i += 1
    del i
    head = tail = Node()
    while queue.next is not None:
        # zdejmuje najmniejszy element z kolejki i dokłada kolejny
        tail.next = queue.next
        tail = tail.next
        queue.next = tail.next
        if cursor is not None:
            node = cursor
            cursor = cursor.next
            notFound = True
            q = queue
            while notFound and q.next is not None:
                if node.val < q.next.val:
                    node.next = q.next
                    notFound = False
                else:
                    q = q.next
            q.next = node
            if notFound:
                node.next = None
        else:
            # Nie ma już co dołożyć: posortowana kolejka stanowi resztę listy.
            tail.next = queue.next
    return head.next


def merge(l1, l2):
    head = tail = Node()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return head.next


def mergeSort(p):
    if p is None or p.next is None:
        return p
    slowCursor = p
    fastCursor = p
    while fastCursor.next and fastCursor.next.next:
        fastCursor = fastCursor.next.next
        slowCursor = slowCursor.next
    part2 = slowCursor.next
    slowCursor.next = None
    return merge(mergeSort(p), mergeSort(part2))


def SortH(p, k):
    if k == 0:
        return p
    twoToK = 2 ** k
    lenn, cursor = 0, p
    while lenn < twoToK and cursor:
        lenn += 1
        cursor = cursor.next
    return selectSort(p, k) if lenn >= twoToK else mergeSort(p)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
