class Objeto:

  def __init__(self, filename):
    self.nPontos = 0
    self.pontos = []
    self.nSuperficies = 0
    self.superficies = []
    self.matrizPontos = montarMatrizPontos()
    lerObjeto(self, filename)
  
  def montarMatrizPontos(self):
    matrizPontos = [[0 for x in range(self.nPontos)] for x in range(4)]
    
    for j in range(self.nPontos):
        matrizPontos[0][j] = pontos[j].x
        matrizPontos[1][j] = pontos[j].y
        matrizPontos[2][j] = pontos[j].z
        matrizPontos[3][j] = 1
    return matrizPontos
  
  def lerObjeto(self, filename):
    f = open(filename)
    pontos = True
      for linha in f:
        linha = linha.strip()
        if pontos and linha != "#":
          self.addPonto(linha)
        elif linha = "#":
          pontos = False
        elif not(pontos):
          self.addSuperficie
  
  def addPonto(self, linha):
    ponto = linha.split(' ')
    novoPonto = Ponto(ponto[0], ponto[1], ponto[2], ponto[3])
    self.pontos.append(novoPonto)
    self.nPontos += 1
    
  def addSuperficie(self, linha):
    superficie = linha.split(' ')
    novaSuperficie = Superficie(superficie[0], superficie[1:], len(superficie)-1]
    self.superficies.append(novaSuperficie)
    self.nSuperficies += 1
