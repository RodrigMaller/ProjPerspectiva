from Tkinter import *

class App:
  
  def __init__(self, master):
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
    
    Label(self.framePlanoProjecao, text="Plano de Projecao").grid(row=0, column=0, columnspan=2)
    Label(self.framePlanoProjecao, text="P1:").grid(row=1, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="P2:").grid(row=2, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="P3:").grid(row=3, column=0, sticky=E)
    
    Label(self.frameObjeto, text="Objeto").grid(row=0, column=0, columnspan=2)
    Label(self.frameObjeto, text="Arq.:").grid(row=1, column=0, sticky=E)
    
    #Entradas
    self.entradaA = Entry(self.framePontoVista).grid(row=1, column=1)
    self.entradaB = Entry(self.framePontoVista).grid(row=2, column=1)
    self.entradaC = Entry(self.framePontoVista).grid(row=3, column=1)
    
    self.entradaP1 = Entry(self.framePlanoProjecao).grid(row=1, column=1)
    self.entradaP2 = Entry(self.framePlanoProjecao).grid(row=2, column=1)
    self.entradaP3 = Entry(self.framePlanoProjecao).grid(row=3, column=1)
    
    self.entradaObjeto = Entry(self.frameObjeto).grid(row=1, column=1)
    
    #Canvas
    self.saidaGrafica = Canvas(self.frameSaidaGrafica, width=640, height=480, bg="white")
    self.saidaGrafica.pack()
    #self.saidaGrafica.create_rectangle(100, 100, 300, 200, activefill="red", width=1)
    
    #Button
    self.botaoProjetar = Button(self.frameObjeto, text="Projetar").grid(row=2, column=0, columnspan=2)
  
  def projetar(self):
    pontoVista = PontoVista(entradaA.get(), entradaB.get(), entradaC.get())
    planoProjecao = PlanoProjecao(entradaP1.get(), entradaP2.get(), entradaP3.get())
    objeto = Objeto(entradaObjeto.get())
    projPerspectiva = ProjPerspectiva(pontoVista, planoProjecao, objeto)
    objeto.matrizPontos = projPerspectiva.projetarObjeto()
