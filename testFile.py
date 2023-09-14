# En este código se encuentran las diferentes pruebas realizadas para comprobar el buen funcionamiento de las funciones que se crearon
# en el archivo matrxVectorsLibrary.py
import matrxVectorsLibrary as mvl
import unittest
import math
class TestVectorsOperations(unittest.TestCase):
    # OPERACIONES EN VECTORES
    def test_SumaVectores(self):
        self.assertEqual(mvl.sumaVect([[(1, -3)], [(-5, 3)], [(0, -1)], [(1, 0)]],
                                      [[(7.5, -1)], [(3, -1)], [(1.5, 1)], [(-1, 1.5)]]),
                         [[(8.5, -4)], [(-2, 2)], [(1.5, 0)], [(0, 1.5)]])
        self.assertEqual(mvl.sumaVect([[(4.5, 7.5)], [(-5.5, -3)], [(-2, 1.5)], [(8, -4)], [(1, -1)]],
                                      [[(1.5, 2.5)], [(1.5, -5)], [(4, -3.5)], [(-6, 7)], [(0, 10)]]),
                         [[(6.0, 10.0)], [(-4.0, -8)], [(2, -2.0)], [(2, 3)], [(1, 9)]])
    def test_InversaVector(self):
        self.assertEqual(mvl.invVect([[(1, -3)], [(-5, 3)], [(0, -1)], [(1, 0)]]),
                         [[(-1, 3)], [(5, -3)], [(0, 1)], [(-1, 0)]])
        self.assertEqual(mvl.invVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [[(-4.5, -7.5)], [(5.5, 3)], [(2, -1.5)], [(-8, 4)], [(-1, 1)]])
    def test_MultiEscalarVector(self):
        self.assertEqual(mvl.multEscVect(0, [[(1, -3)], [(-5, 3)], [(0, -1)], [(1, 0)]]),
                         [[(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]])
        self.assertEqual(mvl.multEscVect(2, [[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [[(9.0, 15.0)], [(-11.0, -6)], [(-4, 3.0)], [(16, -8)], [(2, -2)]])
    def test_TranspuestaVector(self):
        self.assertEqual(mvl.transVect([[(1, -3)], [(-5, 3)], [(0, -1)], [(1, 0)]]),
                         [(1, -3), (-5, 3), (0, -1), (1, 0)])
        self.assertEqual(mvl.transVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [(4.5, 7.5), (-5.5, -3), (-2, 1.5), (8, -4), (1, -1)])
    def test_ConjugadaVector(self):
        self.assertEqual(mvl.conjVect([[(1, -3)], [(-5, 3)], [(0, -1)], [(1, 0)]]),
                         [[(1, 3)], [(-5, -3)], [(0, 1)], [(1, 0)]])
        self.assertEqual(mvl.conjVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [[(4.5, -7.5)], [(-5.5, 3)], [(-2, -1.5)], [(8, 4)], [(1, 1)]])
    def test_AdjuntaVector(self):
        self.assertEqual(mvl.adjMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]]), [[(3, -2), (4, 2)], [(0, -4), (-1, 3)]])
        self.assertEqual(mvl.adjVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [(4.5, -7.5), (-5.5, 3), (-2, -1.5), (8, 4), (1, 1)])
    # -------------------------------------------------------------------------------------------------------------------------
    def test_AccionMatrizVector(self):
        self.assertEqual(mvl.accMtrxVect([[(2,-1),(3,0)],[(-1,-1),(3,1)]],[[(1,1)],[(2,3)]]), [[(9, 10)], [(3, 9)]])
        self.assertEqual(mvl.accMtrxVect([[(3,-4),(1,0),(-1,3)],[(-2,-3),(3,1),(0,0)],[(1,1),(-3,-3),(4,2)]],[[(-1,1)],[(2,2)],[(3,-4)]]),
                         [[(12, 22)], [(9, 9)], [(18, -22)]])
    def test_ProductoInternoVectores(self):
        self.assertEqual(mvl.productInternoVector([[(3,0)],[(1,0)],[(2,0)]],[[(2,0)],[(2,0)],[(-1,0)]]), (6,0))
        self.assertEqual(mvl.productInternoVector([[(-3,2)],[(1,-2)],[(1,0)]],[[(4,-1)],[(3,1)],[(-1,0)]]), (-14,2))
    def test_NormaVector(self):
        self.assertEqual(mvl.normaVector([[(3,0)],[(1,0)],[(2,0)]]), 3.74)
        self.assertEqual(mvl.normaVector([[(-3,2)],[(1,-2)],[(1,0)]]), 1.73)
    def test_DistanciaVectores(self):
        self.assertEqual(mvl.distanciaVectores([[(3,0)],[(1,0)],[(2,0)]],[[(2,0)],[(2,0)],[(-1,0)]]), 3.32)
        self.assertEqual(mvl.distanciaVectores([[(-3,2)],[(1,-2)],[(1,0)]],[[(4,-1)],[(3,1)],[(-1,0)]]), 8.66)
    def test_ValorPropio(self):
        self.assertEqual(mvl.valorPropio([[4, -1],[2, 1]],[[1],[2]]), 2)
        self.assertEqual(mvl.valorPropio([[4, -1],[2, 1]],[[1],[1]]), 3)

    # OPERACIONES EN MATRICES
    def test_SumMatrices(self):
        self.assertEqual(
            mvl.sumMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]], [[(-4, -1), (6, 2)], [(-1, -3), (-2, 5)]]),
            [[(-1, 1), (6, 6)], [(3, -5), (-3, 2)]])
        self.assertEqual(mvl.sumMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]],
                      [[(-1,2),(-3,3),(4,2)],[(3,3),(-4,-1),(-2,-1)],[(0,0),(3,-5),(5,-2)]]),
                         [[(1.5, -1), (-4, 1.5), (4, -1)], [(0, 0), (4, -1), (1, 0)], [(0, 0), (6.5, -3), (-2, -3)]])
    def test_InversaMatriz(self):
        self.assertEqual(mvl.invMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]]), [[(-3, -2), (0, -4)], [(-4, 2), (1, 3)]])
        self.assertEqual(mvl.invMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(-2.5, 3), (1, 1.5), (0, 3)], [(3, 3), (-8, 0), (-3, -1)], [(0, 0), (-3.5, -2), (7, 1)]])
    def test_MultiEscalarMatriz(self):
        self.assertEqual(mvl.multEscMtrx(3, [[(3, 2), (0, 4)], [(4, -2), (-1, -3)]]),
                         [[(9, 6), (0, 12)], [(12, -6), (-3, -9)]])
        self.assertEqual(mvl.multEscMtrx(1.5, [[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(3.75, -4.5), (-1.5, -2.25), (0.0, -4.5)], [(-4.5, -4.5), (12.0, 0.0),
                                (4.5, 1.5)], [(0.0, 0.0), (5.25, 3.0), (-10.5, -1.5)]])
    def test_TranspuestaMatriz(self):
        self.assertEqual(mvl.transVect([[(1, -3)], [(-5, 3)], [(0, -1)], [(1, 0)]]),
                         [(1, -3), (-5, 3), (0, -1), (1, 0)])
        self.assertEqual(mvl.transMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(2.5, -3), (-3, -3), (0, 0)], [(-1, -1.5), (8, 0), (3.5, 2)], [(0, -3), (3, 1), (-7, -1)]])
    def test_ConjugadaMatriz(self):
        self.assertEqual(mvl.conjMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]]), [[(3, -2), (0, -4)], [(4, 2), (-1, 3)]])
        self.assertEqual(mvl.conjMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(2.5, 3), (-1, 1.5), (0, 3)], [(-3, 3), (8, 0), (3, -1)], [(0, 0), (3.5, -2), (-7, 1)]])
    def test_AdjuntaMatriz(self):
        self.assertEqual(mvl.adjMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]]), [[(3, -2), (4, 2)], [(0, -4), (-1, 3)]])
        self.assertEqual(mvl.adjMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(2.5, 3), (-3, 3), (0, 0)], [(-1, 1.5), (8, 0), (3.5, -2)], [(0, 3), (3, -1), (-7, 1)]])
    #--------------------------------------------------------------------------------------------------------------------------
    def test_MultiplicacionMatrices(self):
        self.assertEqual(mvl.multMtrxMtrx([[(0,-2),(0,-4)],[(-3,0),(2,-1)]],[[(0,3),(4,0)],[(2,0),(0,5)]]),
                         [[(6, -8), (20, -8)], [(4, -11), (-7, 10)]])
        self.assertEqual(mvl.multMtrxMtrx([[(3,-2),(-2,4),(3,3)],[(0,-1),(0,0),(-2,-1)]],[[(1,-1),(1,0),(2,3)],[(-2,-2),(0,0),(-1,2)],[(3,1),(4,-2),(-3,-4)]]),
                         [[(19, 3), (21, 4), (9, -24)], [(-6, -6), (-10, -1), (5, 9)]])
    #--------------------------------------------------------------------------------------------------------------------------
    def testCheckHermitian(self):
        self.assertEqual(mvl.checkUnitary([[(1,0),(1,0)],[(1,0),(1,0)]]), False)
        self.assertEqual(mvl.checkUnitary([[(1/math.sqrt(2),0),(1/math.sqrt(2),0)],[(1/math.sqrt(2),0),(-1/math.sqrt(2),0)]]), True)
    def testCheckUnitary(self):
        self.assertEqual(mvl.checkHermitian([[(1/math.sqrt(2),0),(1/math.sqrt(2),0)],[(1/math.sqrt(2),0),(-1/math.sqrt(2),0)]]), True)
        self.assertEqual(mvl.checkHermitian([[(3,-2),(-2,4),(3,3)],[(0,-1),(0,0),(-2,-1)]]), False)
    def testTensorProdc(self):
        self.assertEqual(mvl.prodctTensorMtrx([[(0,0),(1,0)],[(1,0),(0,0)]], [[(3,0),(3,0)],[(3,0),(-3,0)]]),
                         [[(0, 0), (0, 0), (3, 0), (3, 0)], [(0, 0), (0, 0), (-3, 0), (-3, 0)], [(3, 0), (3, 0), (0, 0), (0, 0)], [(-3, 0), (-3, 0), (0, 0), (0, 0)]])
        self.assertEqual(mvl.prodctTensorMtrx([[(3,-2),(-2,4),(3,3)],[(0,-1),(0,0),(-2,-1)]], [[(1,-1),(1,0),(2,3)],[(-2,-2),(0,0),(-1,2)],[(3,1),(4,-2),(-3,-4)]])
            ,[[(1, -5), (1, -5), (1, -5), (2, 6), (2, 6), (2, 6), (6, 0), (6, 0), (6, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(-17, -6), (-17, -6), (-17, -6), (22, -4), (22, -4), (22, -4), (3, -21), (3, -21), (3, -21)], [(-1, -1), (-1, -1), (-1, -1), (0, 0), (0, 0), (0, 0), (-3, 1), (-3, 1), (-3, 1)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(-4, 3), (-4, 3), (-4, 3), (0, 0), (0, 0), (0, 0), (2, 11), (2, 11), (2, 11)]])
if __name__ == '__main__':
    unittest.main()