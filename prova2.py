f = open("C:\\Users\\Eliane\\Desktop\\prova\\prova2.txt", "r")
print(f.read())

A = {4, 8, 12, 16}
B = {5, 10, 15, 20}

uniao = set()
uniao = A.union(B)

print("União de A e B: ", sorted(list(uniao)))

#------------------------------

C = {1, 1, 1, 2, 3, 4, 4, 5}
D = {1, 2, 44, 55, 66, 77}

uniao = set()
uniao = C.union(D)

print("União de C e D: ", sorted(list(uniao)))

#------------------------------

E = {1, 2, 3, 4, 5}
F = {3, 4, 5, 6, 7, 8, 9, 10, 11}

interseccao = set()
interseccao = E.intersection(F)

print("Intersecção de E e F: ", sorted(list(interseccao)))