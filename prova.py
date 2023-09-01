f = open("C:\\Users\\Eliane\\Desktop\\prova.txt", "r")
print(f.read())

A = {3, 5, 67, 7}
B = {1, 2, 3, 4}

uniao = set()
uniao = A.union(B)

print("União de A e B: ", sorted(list(uniao)))

#------------------------------

C = {1, 2, 3, 4, 5}
D = {4, 5}

interseccao = set()
interseccao = C.intersection(D)

print("Intersecção de C e D: ", sorted(list(interseccao)))

#------------------------------

E = {1, 'A', 'C', 34}
F = {'A', 'C', 'D', 23}

diferenca = set()
diferenca = E.difference(F)

print("Diferença de E e F: ", sorted(list(diferenca)))

#------------------------------

G = {3, 4, 5, 5, 'A', 'B', 'R'}
H = {1, 'B', 'C', 'D', 1}

cartesiano = set()

for elemento_g in G:
    for elemento_h in H:
        par_ordenado = (elemento_g, elemento_h)
        cartesiano.add(par_ordenado)

print("Produto cartesiano de G e H: ", cartesiano)