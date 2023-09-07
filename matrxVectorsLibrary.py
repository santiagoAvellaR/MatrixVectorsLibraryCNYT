# En este código se encuentran las diferentes operaciones en espacios de vectoriales, tanto de matrices como de vectores
# Librería que se realizó para la materia CNYT de la Escuela Colombiana de Ingeniería. Durante la semana 3. Fecha: 30/08/23
# Santiago Avellaneda Rodríguez

import complexNumbersLibrary as cl
import math

# Adición de vectores complejos
def sumaVect(v1, v2):
    if len(v1)==len(v2):
        v3 = [[0] for i in range(len(v1))]
        for i in range(len(v1)):
            v3[i][0]= cl.sumCmplx(v1[i][0],v2[i][0])
        return v3
    return "los vectores no tienen misma longitud!"

# Inverso aditivo de un vector de complejos
def invVect(v):
    for i in range(len(v)):
        v[i][0] = cl.invCmplx(v[i][0])
    return v

# Escalar por un vector
def multEscVect(esc, vect):
    for i in range(len(vect)):
        vect[i][0] = cl.multEscCmplx(esc,vect[i][0])
    return vect

# Transpuesta Vector
def transVect(v):
    vr = [0 for i in range(len(v))]
    for i in range(len(v)):
        vr[i] = v[i][0]
    return vr

# Conjugada de un vector
def conjVect(v):
    for i in range(len(v)):
        v[i][0] = cl.conjCmplx(v[i][0])
    return v

# Adjunta/daga de un vector
def adjVect(v):
    return transVect((conjVect(v)))

# Adición de matrices complejas
def sumMtrx(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = [[0 for i in range(len(m1[0]))] for j in range(len(m1))]
        for k in range(len(m1)):
            for l in range(len(m1[0])):
                m3[k][l] = cl.sumCmplx(m1[k][l],m2[k][l])
        return m3
    return "las matrices no tienen las mismas dimensiones!"

# Inversa aditiva de una matriz compleja
def invMtrx(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = cl.invCmplx(m[i][j])
    return m

# Multiplicación de un escalar por una matriz compleja
def multEscMtrx(esc, mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            mtrx[i][j] = cl.multEscCmplx(esc, mtrx[i][j])
    return mtrx

# Transpuesta de una matriz/vector
def transMtrx(m):
    mTr = [[0 for i in range(len(m))] for i in range(len(m[0]))]
    for k in range(len(m)):
        for l in range(len(m[0])):
            mTr[k][l] = m[l][k]
    return mTr

# Conjugado de una matriz
def conjMtrx(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = cl.conjCmplx(m[i][j])
    return m

# Adjunta/Daga de una matriz
def adjMtrx(m):
    return transMtrx(conjMtrx(m))

# Imprimir daga
def printDagaVect(v):
    for i in range(len(v)):
        print(v[i])

# Imprimir un vector
def printVect(v):
    for i in range(len(v)):
        print(v[i][0])

# Imprimir una matriz
def printMtrx(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=" ")
        print()

# ----------------------------------------------------------------------------------------------------------------------
def multMtrxReal(m1, m2):
    if len(m1[0]) == len(m2):
        resultado = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    resultado[i][j] += m1[i][k] * m2[k][j]
        return resultado

def multMtrxMtrx(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = [[(0, 0) for u in range(len(m2[0]))] for v in range(len(m1))]
        for a in range(len(m1)):
            for b in range(len(m2[0])):
                sum = (0, 0)
                for c in range(len(m2)):
                    add = cl.multiCmplx(m1[a][c], m2[c][b])
                    sum = cl.sumCmplx(sum, add)
                m3[a][b] = sum
        return m3

def multMtrxVect(m1, v1):
    if len(m1[0]) == len(v1):
        m3 = [[(0,0)] for v in range(len(v1))]
        sum = (0,0)
        for a in range(len(m1)):
            for b in range(len(v1[0])):
                sum = (0, 0)
                for c in range(len(v1)):
                    add = cl.multiCmplx(m1[a][c], v1[c][b])
                    sum = cl.sumCmplx(sum, add)
                m3[a][b] = sum
        return m3

def accMtrxVect(m, v):
    return multMtrxVect(m, v)

def trazaMtrx(m):
    traza = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                traza += m[i][j]
    return traza

def productoInternoMtrx(m1, m2):
    return trazaMtrx(multMtrxMtrx(adjMtrx(m1),m2))

def productInternoVector(v1, v2):
    if len(v1) == len(v2):
        v1 = conjVect(v1)
        sum = (0,0)
        for i in range(len(v1)):
            add = cl.multiCmplx(v1[i][0], v2[i][0])
            sum = cl.sumCmplx(sum, add)
        return sum

def normaVector(v):
    return round(math.sqrt(productInternoVector(v, v)[0]), 2)

def difVect(v1, v2):
    if len(v1) == len(v2):
        v3 = [[(0,0)] for i in range(len(v1))]
        for i in range(len(v1)):
            v3[i][0] = cl.restCmplx(v1[i][0], v2[i][0])
        return v3

def distanciaVectores(vect1, vect2):
    a = difVect(vect1, vect2)
    return round(math.sqrt(productInternoVector(difVect(vect1, vect2), difVect(vect1, vect2))[0]), 2)

def valorPropio(m, v1):
    if len(m[0]) == len(v1):
        v2 = multMtrxReal(m, v1)
        c = int(v2[0][0]) // int(v1[0][0])
        return c

def casosPrueba2():
    print(multMtrxMtrx([[(3,-2),(-2,4),(3,3)],[(0,-1),(0,0),(-2,-1)]],[[(1,-1),(1,0),(2,3)],[(-2,-2),(0,0),(-1,2)],[(3,1),(4,-2),(-3,-4)]]))

casosPrueba2()

def casosPrueba1():
    # Para el vector 1x4 [[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]
    print("1. Suma Vector 1")
    printVect(sumaVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]], [[(7.5,-1)],[(3,-1)],[(1.5,1)],[(-1,1.5)]]))
    print("2. Inverso aditivo Vector 1")
    printVect(invVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]))
    print("3. Multiplicación escalar x vector 1")
    printVect(multEscVect(0, [[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]))
    print("7. Transpuesta Vector 1")
    printMtrx(transVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]))
    print("8. Conjugado Vector 1")
    printVect(conjVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]))
    print("9. Daga Vector 1")
    printDagaVect(adjVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]))
    print()

    # Para la matrriz 2x2 [[(3,2),(0,4)],[(4,-2),(-1,-3)]]
    print("4. Suma Matriz 1")
    printMtrx(sumMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]], [[(-4, -1), (6, 2)], [(-1, -3), (-2, 5)]]))
    print("5. Inverso aditivo Matriz 1")
    printMtrx(invMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]))
    print("6. Multiplicacion escalar x Matriz 1")
    printMtrx(multEscMtrx(3, [[(3,2),(0,4)],[(4,-2),(-1,-3)]]))
    print("7. Transpuesta Matriz 1")
    printMtrx(transMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]))
    print("8. Conjugado Matriz 1")
    printMtrx(conjMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]))
    print("9. Daga Matriz 1")
    printMtrx(adjMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]))
    print()

    # Para el vector 1x5 [[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]
    print("1. Suma Vector 2")
    printVect(sumaVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]],
                       [[(1.5, 2.5)], [(1.5, -5)], [(4, -3.5)], [(-6, 7)], [(0, 10)]]))
    print("2. Inverso aditivo Vector 2")
    printVect(invVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]))
    print("3. Multiplicación escalar x vector 2")
    printVect(multEscVect(2, [[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]))
    print("7. Transpuesta Vector 2")
    printMtrx(transVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]))
    print("8. Conjugado Vector 2")
    printVect(conjVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]))
    print("9. Daga Vector 2")
    printDagaVect(adjVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]))
    print()

    # Para la matriz 3x3 [[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]
    print("Suma Matriz 2")
    printMtrx(sumMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]],
                      [[(-1,2),(-3,3),(4,2)],[(3,3),(-4,-1),(-2,-1)],[(0,0),(3,-5),(5,-2)]]))
    print("Inverso Matriz 2")
    printMtrx(invMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]))
    print("Multiplicacion escalar x Matriz 2")
    printMtrx(multEscMtrx(1.5, [[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]))
    print("Transpuesta Matriz 2")
    printMtrx(transMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]))
    print("Conjugado Matriz 2")
    printMtrx(conjMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]))
    print("Daga Matriz 2")
    printMtrx(adjMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]))
    print()