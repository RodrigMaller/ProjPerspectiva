class Objeto:

  def __init__(self, filename):
    self.nPontos = 0
    self.pontos = []
    self.nSuperficies = 0
    self.superficies = []
    self.lerObjeto(filename)
    self.matrizPontos = self.montarMatrizPontos()
  
  def montarMatrizPontos(self):
    matrizPontos = [[0 for x in range(self.nPontos)] for x in range(4)]
    
    for j in range(self.nPontos):
        matrizPontos[0][j] = self.pontos[j][0]
        matrizPontos[1][j] = self.pontos[j][1]
        matrizPontos[2][j] = self.pontos[j][2]
        matrizPontos[3][j] = 1
    return matrizPontos
  
  def lerObjeto(self, filename):
    f = open(filename)
    pontos = True
    for linha in f:
      linha = linha.strip()     
      if pontos and linha != "#":
        self.addPonto(linha)
      elif linha == "#":
        pontos = False
      elif not(pontos):
        self.addSuperficie(linha)
      
  def addPonto(self, linha):
    ponto = linha.split(' ')
    for i in range(len(ponto)):
      ponto[i] = float(ponto[i])
    self.pontos.append(ponto)
    self.nPontos += 1
    
  def addSuperficie(self, linha):
    superficie = linha.split(' ')
    for i in range(len(superficie)):
      superficie[i] = float(superficie[i])
    self.superficies.append(superficie)
    self.nSuperficies += 1
