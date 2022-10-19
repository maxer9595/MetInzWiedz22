import numpy as np

""" def wyznacznik_macierzy(A):
    wynik = 0
    indeksy = list(range(len(A)))
    if (len(A) == 2):
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        for ind in indeksy:
            Ac = A.copy()
            Ac = np.delete(Ac ,0 ,0)
            height = len(Ac)
            
            for i in range(height):
                Ac[i] = Ac[i][0:ind] + Ac[i][ind+1:]
                
            znak = (-1) ** (ind % 2)
            podmacierz = wyznacznik_macierzy(Ac)
            wynik += znak * podmacierz * A[0][ind]
    return wynik


M1 = [[-2,2,-3],[-1,5,3],[2,0,-1]]
print(wyznacznik_macierzy(M1))
W1np = np.linalg.det(M1)
M1 = wyznacznik_macierzy(M1)
print(M1, W1np) """


def wyznacznik_macierzy(A):
    wynik = 0
    indeksy = list(range(len(A)))
    if (len(A) == 2):
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        for ind in indeksy:
            Ac = A.copy()
            Ac = np.delete(Ac ,0 ,0)
            Ac = np.delete(Ac ,ind ,1)
            znak = (-1) ** (ind % 2)
            podmacierz = wyznacznik_macierzy(Ac)
            wynik += znak * podmacierz * A[0][ind]
    return wynik

M1 = [[-2,2,-3],[-1,5,3],[2,0,-1]]
M2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
M3 = [[1,2,3,4,1],[8,5,6,7,2],[9,12,10,11,3],[13,14,16,15,4],[10,8,6,4,2]]

W1np = np.linalg.det(M1)
W2np = np.linalg.det(M2)
W3np = np.linalg.det(M3)

M1w = wyznacznik_macierzy(M1)
M2w = wyznacznik_macierzy(M2)
M3w = wyznacznik_macierzy(M3)

print(M1w, W1np)
print(M2w, W2np)
print(M3w, W3np)
