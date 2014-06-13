class Viewport:
  
  def __init__(self, janelaMundo, janelaViewport, matrizPontos):
    self.uMin = janelaViewport.xMin
    self.uMax = janelaViewport.xMax
    self.vMin = janelaViewport.yMin
    self.vMax = janelaViewport.yMax
    self.xMin = janelaMundo.xMin
    self.xMax = janelaMundo.xMax
    self.yMin = janelaMundo.yMin
    self.yMax = janelaMundo.yMax
    self.janelaViewport = janelaViewport
    self.matrizPontos = matrizPontos
    self.matrizViewport = self.montarMatrizViewport()
  
  def montarMatrizViewport(self):
    matriz = [[0 for x in range(3)] for x in range(3)]
    
    matriz[0][0] = (self.uMax-self.uMin)/(self.xMax-self.xMin)
    matriz[1][1] = (self.vMax-self.vMin)/(self.yMax-self.yMin)
    matriz[0][2] = (-self.xMin * ((self.uMax-self.uMin)/(self.xMax-self.xMin))) + self.uMin
    matriz[1][2] = (-self.yMin * ((self.vMax-self.vMin)/(self.yMax-self.yMin))) + self.vMin
    matriz[2][2] = 1
    
    return matriz
  
  def transfViewport(self):
    matrizResultado = [[0 for x in range(len(self.matrizPontos[0]))] for x in range(3)]
    
    for m in range(3):
      for p in range(len(self.matrizPontos[0])):
        for n in range(3):
          matrizResultado[m][p] += self.matrizViewport[m][n] * self.matrizPontos[n][p]
                      
    return matrizResultado
