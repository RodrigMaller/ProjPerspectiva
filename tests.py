import sys
import random
import unittest

sys.path.append("Algoritmos/")

from projPerspectiva import ProjPerspectiva
from viewport import Viewport 

sys.path.append("Estruturas/")
from objeto import Objeto
from pontoVista import PontoVista
from planoProjecao import PlanoProjecao

class TestSequenceFunctions(unittest.TestCase):

#    def setUp(self):
 #     self.seq = range(10)

    def test_casa3_objeto(self):
      self.obj_casa3 = Objeto("./testes/casa3")
      self.assertEqual(self.obj_casa3.nPontos, 30)
      self.assertEqual(self.obj_casa3.nSuperficies, 15)

    def test_casa3_proj_perspectiva(self):
      self.obj_casa3 = Objeto("./testes/casa3")
      self.pp_casa3 = ProjPerspectiva(PontoVista(5,5,3),PlanoProjecao([0,0,0],[1,0,0],[0,1,0]),self.obj_casa3)
      self.assertEqual(self.pp_casa3.matrizProjecao[0][0], -3)
      self.assertEqual(self.pp_casa3.matrizProjecao[0][1], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[0][2], 5)
      self.assertEqual(self.pp_casa3.matrizProjecao[0][3], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[1][0], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[1][1], -3)
      self.assertEqual(self.pp_casa3.matrizProjecao[1][2], 5)
      self.assertEqual(self.pp_casa3.matrizProjecao[1][3], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[2][0], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[2][1], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[2][2], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[2][3], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[3][0], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[3][1], 0)
      self.assertEqual(self.pp_casa3.matrizProjecao[3][2], 1)
      self.assertEqual(self.pp_casa3.matrizProjecao[3][3], -3)

        
if __name__ == '__main__':
    unittest.main()
