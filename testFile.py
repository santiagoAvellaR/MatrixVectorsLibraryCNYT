# En este código se encuentran las diferentes pruebas realizadas para comprobar el buen funcionamiento de las funciones que se crearon
# en el archivo matrxVectorsLibrary.py
import matrxVectorsLibrary as mvl
import unittest
class TestVectorsOperations(unittest.TestCase):
    def testOperations(self):
        # Para el vector 1
        self.assertEqual(mvl.sumaVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]], [[(7.5,-1)],[(3,-1)],[(1.5,1)],[(-1,1.5)]]),
                         [[(8.5, -4)], [(-2, 2)], [(1.5, 0)], [(0, 1.5)]])
        self.assertEqual(mvl.invVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]), [[(-1, 3)], [(5, -3)], [(0, 1)], [(-1, 0)]])
        self.assertEqual(mvl.multEscVect(0, [[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]), [[(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]])
        self.assertEqual(mvl.transVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]), [(1, -3), (-5, 3), (0, -1), (1, 0)])
        self.assertEqual(mvl.conjVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]), [[(1, 3)], [(-5, -3)], [(0, 1)], [(1, 0)]])
        self.assertEqual(mvl.adjVect([[(1,-3)],[(-5,3)],[(0,-1)],[(1,0)]]), [(1, 3), (-5, -3), (0, 1), (1, 0)])

        # Para la matriz 1
        self.assertEqual(mvl.sumMtrx([[(3, 2), (0, 4)], [(4, -2), (-1, -3)]], [[(-4, -1), (6, 2)], [(-1, -3), (-2, 5)]]),
                         [[(-1, 1), (6, 6)], [(3, -5), (-3, 2)]])
        self.assertEqual(mvl.invMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]), [[(-3, -2), (0, -4)], [(-4, 2), (1, 3)]])
        self.assertEqual(mvl.multEscMtrx(3, [[(3,2),(0,4)],[(4,-2),(-1,-3)]]), [[(9, 6), (0, 12)], [(12, -6), (-3, -9)]])
        self.assertEqual(mvl.transMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]), [[(3, 2), (4, -2)], [(0, 4), (-1, -3)]])
        self.assertEqual(mvl.conjMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]), [[(3, -2), (0, -4)], [(4, 2), (-1, 3)]])
        self.assertEqual(mvl.adjMtrx([[(3,2),(0,4)],[(4,-2),(-1,-3)]]), [[(3, -2), (4, 2)], [(0, -4), (-1, 3)]])

        # Para el vector 2
        self.assertEqual(mvl.sumaVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]],
                       [[(1.5, 2.5)], [(1.5, -5)], [(4, -3.5)], [(-6, 7)], [(0, 10)]]),
                         [[(6.0, 10.0)], [(-4.0, -8)], [(2, -2.0)], [(2, 3)], [(1, 9)]])
        self.assertEqual(mvl.invVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [[(-4.5, -7.5)], [(5.5, 3)], [(2, -1.5)], [(-8, 4)], [(-1, 1)]])
        self.assertEqual(mvl.multEscVect(2, [[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [[(9.0, 15.0)], [(-11.0, -6)], [(-4, 3.0)], [(16, -8)], [(2, -2)]])
        self.assertEqual(mvl.transVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [(4.5, 7.5), (-5.5, -3), (-2, 1.5), (8, -4), (1, -1)])
        self.assertEqual(mvl.conjVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [[(4.5, -7.5)], [(-5.5, 3)], [(-2, -1.5)], [(8, 4)], [(1, 1)]])
        self.assertEqual(mvl.adjVect([[(4.5,7.5)],[(-5.5,-3)],[(-2,1.5)],[(8,-4)],[(1,-1)]]),
                         [(4.5, -7.5), (-5.5, 3), (-2, -1.5), (8, 4), (1, 1)])

        # Para la matriz 2
        self.assertEqual(mvl.sumMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]],
                      [[(-1,2),(-3,3),(4,2)],[(3,3),(-4,-1),(-2,-1)],[(0,0),(3,-5),(5,-2)]]),
                         [[(1.5, -1), (-4, 1.5), (4, -1)], [(0, 0), (4, -1), (1, 0)], [(0, 0), (6.5, -3), (-2, -3)]])
        self.assertEqual(mvl.invMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(-2.5, 3), (1, 1.5), (0, 3)], [(3, 3), (-8, 0), (-3, -1)], [(0, 0), (-3.5, -2), (7, 1)]])
        self.assertEqual(mvl.multEscMtrx(1.5, [[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(3.75, -4.5), (-1.5, -2.25), (0.0, -4.5)], [(-4.5, -4.5), (12.0, 0.0),
                                (4.5, 1.5)], [(0.0, 0.0), (5.25, 3.0), (-10.5, -1.5)]])
        self.assertEqual(mvl.transMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(2.5, -3), (-3, -3), (0, 0)], [(-1, -1.5), (8, 0), (3.5, 2)], [(0, -3), (3, 1), (-7, -1)]])
        self.assertEqual(mvl.conjMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(2.5, 3), (-1, 1.5), (0, 3)], [(-3, 3), (8, 0), (3, -1)], [(0, 0), (3.5, -2), (-7, 1)]])
        self.assertEqual(mvl.adjMtrx([[(2.5,-3),(-1,-1.5),(0,-3)],[(-3,-3),(8,0),(3,1)],[(0,0),(3.5,2),(-7,-1)]]),
                         [[(2.5, 3), (-3, 3), (0, 0)], [(-1, 1.5), (8, 0), (3.5, -2)], [(0, 3), (3, -1), (-7, 1)]])

if __name__ == '__main__':
    unittest.main()