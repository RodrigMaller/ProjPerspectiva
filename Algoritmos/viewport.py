class Viewport:
  
  def __init__(self, janelaMundo, janelaViewport, matrizPontos, objeto):
    self.janelaMundo = janelaMundo
    self.janelaViewport = janelaViewport
    self.matrizPontos = matrizPontos
    self.objeto = objeto
    self.matrizViewport = montarMatrizViewport()
  
  def montarMatrizViewport(self):
    matriz = [[0 for x in range(3)] for x in range(3)]
    
    matriz[0][0] = (self.uMax-self.uMin)/(self.xMax-self.xMin)
    matriz[1][1] = (self.vMax-self.vMin)/(self.yMax-self.yMin)
    matriz[0][2] = ((self.uMax-self.uMin)/(self.xMax-self.xMin)) + uMin
    matriz[1][2] = ((self.vMax-self.vMin)/(self.yMax-self.yMin)) + vMin
    matriz[2][2] = 1
    
    return matriz
  
  def transfViewport(self):
    matrizResultado = [[0 for x in range(3)] for x in range(3)]
    
    matrizResultado = [[sum(self.matrizViewport[m][n] * self.matrizPontos[n][p] for n in range(3)) \
                      for p in range(self.objeto.nVertices)] for m in range(3)]
                      
    return matrizResultado
