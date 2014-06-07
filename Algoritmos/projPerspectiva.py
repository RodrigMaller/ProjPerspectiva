class ProjPerspectiva:

  def __init__(self, pontoVista, planoProjecao, objeto):
    self.pontoVista = pontoVista.A
    self.planoProjecao = planoProjecao
    self.objeto = objeto
    self.matrizProjecao = montarMatrizProjecao()
    self.matrizPontos = montarMatrizPontos()
    
  def montarMatrizProjecao(self):
    matriz = [[0 for x in range(4)] for x in range(4)]
    
    d0 = self.planoProjecao.R0[0]*self.planoProjecao.vetorNormal[0] \
         + self.planoProjecao.R0[1]*self.planoProjecao.vetorNormal[1] \
         + self.planoProjecao.R0[2]*self.planoProjecao.vetorNormal[2]
    d1 = self.pontoVista.A*self.planoProjecao.vetorNormal[0] \
         + self.pontoVista.B*self.planoProjecao.vetorNormal[1] \
         + self.pontoVista.C*self.planoProjecao.vetorNormal[2]
    d = d0 - d1
    
    #   Matrix de Projeção = 
    #[[d+ANx, ANy,  ANz,  -Ad0],
    # [BNx,  d+BNy, BNz,  -Bd0],
    # [CNx,   CNy, d+CNz, -Cd0],
    # [Nx,    Ny,   Nz,   -d1 ]]
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
    
    return matriz
  
  def montarMatrizPontos(self):
    matrizPontos = [[0 for x in range(self.objeto.nVertices)] for x in range(4)]
    
    for j in range(self.objeto.nVertices):
        matrizPontos[0][j] = X[j]
        matrizPontos[1][j] = Y[j]
        matrizPontos[2][j] = Z[j]
        matrizPontos[3][j] = 1
  
  def projetarObjeto(self):
    matrizResultado = [[0 for x in range(4)] for x in range(4)]
    
    matrizResultado = [[sum(self.matrizProjecao[m][n] * self.matrizPontos[n][p] for n in range(4)) \
                      for p in range(self.objeto.nVertices)] for m in range(4)]
    
