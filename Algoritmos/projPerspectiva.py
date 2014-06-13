class ProjPerspectiva:

  def __init__(self, pontoVista, planoProjecao, objeto):
    self.pontoVista = pontoVista
    self.planoProjecao = planoProjecao
    self.objeto = objeto
    self.matrizProjecao = self.montarMatrizProjecao()
    
  def montarMatrizProjecao(self):
    matriz = [[0 for x in range(4)] for x in range(4)]
    
    d0 = self.planoProjecao.P1[0]*self.planoProjecao.vetorNormal[0] \
         + self.planoProjecao.P1[1]*self.planoProjecao.vetorNormal[1] \
         + self.planoProjecao.P1[2]*self.planoProjecao.vetorNormal[2]
    d1 = self.pontoVista.A*self.planoProjecao.vetorNormal[0] \
         + self.pontoVista.B*self.planoProjecao.vetorNormal[1] \
         + self.pontoVista.C*self.planoProjecao.vetorNormal[2]
    d = d0 - d1

    print(d0, d1, d)
    
    matriz[0][0] = d + self.pontoVista.A*self.planoProjecao.vetorNormal[0]    
    matriz[0][1] = self.pontoVista.A*self.planoProjecao.vetorNormal[1]
    matriz[0][2] = self.pontoVista.A*self.planoProjecao.vetorNormal[2]
    matriz[0][3] = -self.pontoVista.A*d0
    matriz[1][0] = self.pontoVista.B*self.planoProjecao.vetorNormal[0]
    matriz[1][1] = d + self.pontoVista.B*self.planoProjecao.vetorNormal[1]
    matriz[1][2] = self.pontoVista.B*self.planoProjecao.vetorNormal[2]
    matriz[1][3] = -self.pontoVista.B*d0
    matriz[2][0] = self.pontoVista.C*self.planoProjecao.vetorNormal[0]
    matriz[2][1] = self.pontoVista.C*self.planoProjecao.vetorNormal[1]
    matriz[2][2] = d + self.pontoVista.C*self.planoProjecao.vetorNormal[2]
    matriz[2][3] = -self.pontoVista.C*d0
    matriz[3][0] = self.planoProjecao.vetorNormal[0]
    matriz[3][1] = self.planoProjecao.vetorNormal[1]
    matriz[3][2] = self.planoProjecao.vetorNormal[2]
    matriz[3][3] = -d1
    
  #  for m in range(4):
   #     for n in range(4):
    #        print(matriz[m][n]);


    return matriz
  
  def projetarObjeto(self):
    matrizResultado = [[0 for x in range(len(self.objeto.matrizPontos[0]))] for x in range(4)]
    
    for m in range(4):
      for p in range(len(self.objeto.matrizPontos[0])):
        for n in range(4):
          matrizResultado[m][p] += self.matrizProjecao[m][n] * self.objeto.matrizPontos[n][p]
    return matrizResultado
    
