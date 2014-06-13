from Tkinter import *
from tkFileDialog import askopenfilename
sys.path.append("Algoritmos/")
from projPerspectiva import ProjPerspectiva
from viewport import Viewport
sys.path.append("Estruturas/")
from objeto import Objeto
from pontoVista import PontoVista
from planoProjecao import PlanoProjecao
from janela import Janela

class App:
  
  def __init__(self, master):
    self.objeto = object
    #init Frames
    self.framePontoVista = Frame(master, relief=FLAT, borderwidth=2)
    self.framePlanoProjecao = Frame(master, relief=FLAT, borderwidth=2)
    self.frameObjeto = Frame(master, relief=FLAT, borderwidth=2)
    self.frameSaidaGrafica = Frame(master, relief=SUNKEN, borderwidth=2, bg="black")
    
    #Griding Frames
    self.framePontoVista.grid(row=0, column=0)
    self.framePlanoProjecao.grid(row=1, column=0)
    self.frameObjeto.grid(row=2, column=0)
    self.frameSaidaGrafica.grid(row=0, column=1, rowspan=4)
    
    #Labels
    Label(self.framePontoVista, text="Ponto de Vista").grid(row=0, column=0, columnspan=2)
    Label(self.framePontoVista, text="A:").grid(row=1, column=0, sticky=E)
    Label(self.framePontoVista, text="B:").grid(row=2, column=0, sticky=E)
    Label(self.framePontoVista, text="C:").grid(row=3, column=0, sticky=E)
    
    Label(self.framePlanoProjecao, text="Plano de Projecao").grid(row=0, column=0, columnspan=4)
    Label(self.framePlanoProjecao, text="P1:").grid(row=1, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="P2:").grid(row=2, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="P3:").grid(row=3, column=0, sticky=E)
    
    Label(self.frameObjeto, text="Objeto").grid(row=0, column=0, columnspan=2)
    
    #Entradas
    self.entradaA = Entry(self.framePontoVista, width=3)
    self.entradaA.insert(0, "3")
    self.entradaB = Entry(self.framePontoVista, width=3)
    self.entradaB.insert(0, "3")
    self.entradaC = Entry(self.framePontoVista, width=3)
    self.entradaC.insert(0, "3")
    
    self.entradaP1X = Entry(self.framePlanoProjecao, width=3)
    self.entradaP1Y = Entry(self.framePlanoProjecao, width=3)
    self.entradaP1Z = Entry(self.framePlanoProjecao, width=3)
    self.entradaP2X = Entry(self.framePlanoProjecao, width=3)
    self.entradaP2Y = Entry(self.framePlanoProjecao, width=3)
    self.entradaP2Z = Entry(self.framePlanoProjecao, width=3)
    self.entradaP3X = Entry(self.framePlanoProjecao, width=3)
    self.entradaP3Y = Entry(self.framePlanoProjecao, width=3)
    self.entradaP3Z = Entry(self.framePlanoProjecao, width=3)
    
    #Griding Entradas
    self.entradaA.grid(row=1, column=1)
    self.entradaB.grid(row=2, column=1)
    self.entradaC.grid(row=3, column=1)
    
    self.entradaP1X.grid(row=1, column=1)
    self.entradaP1Y.grid(row=1, column=2)
    self.entradaP1Z.grid(row=1, column=3)
    self.entradaP2X.grid(row=2, column=1)
    self.entradaP2Y.grid(row=2, column=2)
    self.entradaP2Z.grid(row=2, column=3)
    self.entradaP3X.grid(row=3, column=1)
    self.entradaP3Y.grid(row=3, column=2)
    self.entradaP3Z.grid(row=3, column=3)
    
    #Canvas
    self.saidaGrafica = Canvas(self.frameSaidaGrafica, width=640, height=480, bg="white")
    self.saidaGrafica.pack()
    #self.saidaGrafica.create_rectangle(100, 100, 300, 200, activefill="red", width=1)
    
    #Button
    self.botaoObjeto = Button(self.frameObjeto, text="Escolher Objeto", command=self.arquivoObjeto).grid(row=2, column=0, columnspan=2)
    self.botaoProjetar = Button(self.frameObjeto, text="Projetar", command=self.projetar).grid(row=3, column=0, columnspan=2)
  
  def cartesiano(self, matriz):
    nMatriz = [[0 for x in range(len(self.objeto.matrizPontos[0]))] for x in range(3)]
    
    for j in range(len(matriz[0])):
      nMatriz[0][j] = matriz[0][j] / matriz[3][j]
      nMatriz[1][j] = matriz[1][j] / matriz[3][j]
      nMatriz[2][j] = 1
    return nMatriz
  
  def reflexao(self, matriz):
    nMatriz = matriz
    
    for j in range(len(matriz[0])):
      nMatriz[1][j] = -matriz[1][j]
    return nMatriz
  
  def desenhar(self, matriz):
    self.saidaGrafica.delete(ALL)
    for sup in self.objeto.superficies:
      for i in range(len(sup)):
        if (i == len(sup)-1):
          ponto1 = sup[i]
          ponto2 = sup[0]
        else:
          ponto1 = sup[i]
          ponto2 = sup[i+1]
        self.saidaGrafica.create_line(matriz[0][ponto1], matriz[1][ponto1], matriz[0][ponto2], matriz[1][ponto2])
  
  def arquivoObjeto(self):
    self.filename = askopenfilename()
    if self.objeto:
      del self.objeto
    self.objeto = Objeto(self.filename)
  
  def projetar(self):
    self.pontoVista = PontoVista(int(self.entradaA.get()), int(self.entradaB.get()), int(self.entradaC.get()))
    ponto1 = [int(self.entradaP1X.get()), int(self.entradaP1Y.get()), int(self.entradaP1Z.get())]
    ponto2 = [int(self.entradaP2X.get()), int(self.entradaP2Y.get()), int(self.entradaP2Z.get())]
    ponto3 = [int(self.entradaP3X.get()), int(self.entradaP3Y.get()), int(self.entradaP3Z.get())]
    self.planoProjecao = PlanoProjecao(ponto1, ponto2, ponto3)
    self.projPerspectiva = ProjPerspectiva(self.pontoVista, self.planoProjecao, self.objeto)
    matriz = self.projPerspectiva.projetarObjeto()
    cMatriz = self.cartesiano(matriz)
    rMatriz = self.reflexao(cMatriz)
    self.janelaMundo = Janela(min(rMatriz[0]), min(rMatriz[1]), max(rMatriz[0]), max(rMatriz[1]))
    self.janelaViewport = Janela(20, 20, 620, 460)
    self.viewport = Viewport(self.janelaMundo, self.janelaViewport, rMatriz)
    matrizFinal = self.viewport.transfViewport()
    self.desenhar(matrizFinal)
