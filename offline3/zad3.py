from zad3testy import runtests

# Jan Pulkowski
# (420313)
# Obliczam sumy prefiksowe liczby punktów położonych na danej wartości dla obu współrzędnej
# Za pomocą sum prefiksowych wyznaczam dla każdego punktu różnicę między
# ilością punktów dominowanych przez niego a dominujących go.
# Element maksymalny nie będzie dominowany przez żaden punkt, więc wyliczona
# dla niego wartość jest równa liczbie punktów dominowanych przez niego.
# Lider zbioru będzie elementem maksymalnym o największej wyliczonej wartości.
#
# Wyżej wspomniana różnica jest wyliczana dla punktu p0 w następujący sposób
# aDb <=> a[0] > b[0] and a[1] > b[1];
# val = #{ p in P : p0 D p } - #{ p in P : p D p0 } =
# = -(#{ p in P : p D p0 } + #{p0}) + #{ p in P : p0 D p } + 1 =
# = - (|P| - #{ p in P : p[0] < p0[0] or p[1] < p0[1] }) + #{ p in P : p0 D p } + 1 =
# = #{ p in P : p0 D p } + #{ p in P : p[0] < p0[0] or p[1] < p0[1]} - |P| + 1 =
# = #{ p in P : p[0] < p0[0] and p[1] < p0[1] } + #{ p in P : p[0] < p0[0] or p[1] < p0[1] } - |P| + 1 =
# = #{ p in P : p[0] < p0[0] } + #{ p in P : p[1] < p0[1] } - |P| + 1
#
# więc wartość jest wyliczana przez: prefixX[x - 1] + prefixY[y - 1] - len(P) + 1

class Record:
    def __init__(self):
        self.pt = (-1,-1)
        self.maximised = -1


def dominance(P):
    prefixX = [0] * (len(P) + 1)
    prefixY = [0] * (len(P) + 1)
    for pt in P:
        prefixX[pt[0]] += 1
        prefixY[pt[1]] += 1
    for i in range(1, len(P) + 1):
        prefixX[i] += prefixX[i - 1]
        prefixY[i] += prefixY[i - 1]
    result = Record()
    for pt in P:
        x, y = pt
        val = prefixX[x - 1] + prefixY[y - 1] - len(P) + 1
        if val > result.maximised:
            result.pt = pt
            result.maximised = val
    return result.maximised

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
