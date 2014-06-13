class PlanoProjecao:

  def __init__(self, P1, P2, P3):
    self.P1 = P1
    self.P2 = P2
    self.P3 = P3
    self.vetorNormal = self.calcularVetorNormal()
    
  def calcularVetorNormal(self):
    V12 = [0, 0, 0]
    V13 = [0, 0, 0]
    normal = [0, 0, 0]
    
    for i in range(3):
      V12[i] = self.P2[i] - self.P1[i]
      V13[i] = self.P3[i] - self.P1[i]
    normal[0] = V12[1]*V13[2] - V12[2]*V13[1]
    normal[1] = V12[2]*V13[0] - V12[0]*V13[2]
    normal[2] = V12[0]*V13[1] - V12[1]*V13[0]
    return normal
