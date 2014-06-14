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

    def test_casa3_proj_calculada(self):
      self.obj_casa3 = Objeto("./testes/casa3")
      self.pp_casa3 = ProjPerspectiva(PontoVista(5,5,3),PlanoProjecao([0,0,0],[1,0,0],[0,1,0]),self.obj_casa3)
      self.obj_projetado = self.pp_casa3.projetarObjeto();
      self.assertEqual(self.obj_projetado[0][0], 0)
      self.assertEqual(self.obj_projetado[0][1], -1.5)
      self.assertEqual(self.obj_projetado[0][2], -6.5)
      self.assertEqual(self.obj_projetado[0][3], -12.5)      
      self.assertEqual(self.obj_projetado[0][4], -7.5)
      self.assertEqual(self.obj_projetado[0][5], -18)
      self.assertEqual(self.obj_projetado[0][6], 32)
      self.assertEqual(self.obj_projetado[0][7], 50)
      self.assertEqual(self.obj_projetado[0][8], 50)
      self.assertEqual(self.obj_projetado[0][9], 0)

      self.assertEqual(self.obj_projetado[1][0], 0)
      self.assertEqual(self.obj_projetado[1][1], 0)
      self.assertEqual(self.obj_projetado[1][2], -5)
      self.assertEqual(self.obj_projetado[1][3], -5)      
      self.assertEqual(self.obj_projetado[1][4], 0)
      self.assertEqual(self.obj_projetado[1][5], 0)
      self.assertEqual(self.obj_projetado[1][6], 50)
      self.assertEqual(self.obj_projetado[1][7], 50)
      self.assertEqual(self.obj_projetado[1][8], 41)
      self.assertEqual(self.obj_projetado[1][9], -9)

      self.assertEqual(self.obj_projetado[2][0], 0)
      self.assertEqual(self.obj_projetado[2][1], 0)
      self.assertEqual(self.obj_projetado[2][2], 0)
      self.assertEqual(self.obj_projetado[2][3], 0)      
      self.assertEqual(self.obj_projetado[2][4], 0)
      self.assertEqual(self.obj_projetado[2][5], 0)
      self.assertEqual(self.obj_projetado[2][6], 0)
      self.assertEqual(self.obj_projetado[2][7], 0)
      self.assertEqual(self.obj_projetado[2][8], 0)
      self.assertEqual(self.obj_projetado[2][9], 0)
      
      self.assertEqual(self.obj_projetado[0][0], -3)
      self.assertEqual(self.obj_projetado[0][1], -3)
      self.assertEqual(self.obj_projetado[0][2], -4)
      self.assertEqual(self.obj_projetado[0][3], -4)      
      self.assertEqual(self.obj_projetado[0][4], -3)
      self.assertEqual(self.obj_projetado[0][5], -3)
      self.assertEqual(self.obj_projetado[0][6], 7)
      self.assertEqual(self.obj_projetado[0][7], 7)
      self.assertEqual(self.obj_projetado[0][8], 7)
      self.assertEqual(self.obj_projetado[0][9], -3)
   
if __name__ == '__main__':
    unittest.main()
