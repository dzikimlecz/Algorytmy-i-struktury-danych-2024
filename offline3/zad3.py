from zad3testy import runtests


def countingSort(points: list, key: int) -> list:
  n = len(points)
  temp = [[0] for _ in range(n + 1)]
  for pt in points:
    k = max(pt[0], pt[1]) if key else min(pt[0], pt[1])
    temp[k][0] += 1
    temp[k].append(pt)
  for i in range(1, len(temp)):
    temp[i][0] += temp[i - 1][0]
  result = [0] * n
  for i in range(n, -1, -1):
    record = temp[i]
    while len(record) > 1:
      record[0] -= 1
      result[record[0]] = record.pop()
  return result


def radixSort(points: list) -> list:
  return countingSort(countingSort(points, 1), 0)


def dominanceRelation(p1, p2) -> int:
  if p1[0] < p2[0] and p1[1] < p2[1]:
    return -1
  if p1[0] > p2[0] and p1[1] > p2[1]:
    return 1
  return 0


def heura(l: list) -> int:
  sortd = radixSort(l)
  check = sortd.pop()
  res = 0
  for e in sortd:
    r = dominanceRelation(check, e)
    if r:
      res += 1
  return res


def dominance(P):
  # tu prosze wpisac wlasna implementacje
  return heura(P)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
