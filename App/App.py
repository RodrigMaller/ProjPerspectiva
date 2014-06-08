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
    Label(self.framePlanoProjecao, text="X:").grid(row=1, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="Y:").grid(row=2, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="Z:").grid(row=3, column=0, sticky=E)
    
    Label(self.frameObjeto, text="Objeto").grid(row=0, column=0, columnspan=4)
    Label(self.frameObjeto, text="Num. Vertices:").grid(row=1, column=0, sticky=E, columnspan=2)
    Label(self.frameObjeto, text="X").grid(row=2, column=1)
    Label(self.frameObjeto, text="Y").grid(row=2, column=2)
    Label(self.frameObjeto, text="Z").grid(row=2, column=3)
    Label(self.frameObjeto, text="P1:").grid(row=3, column=0, sticky=E)
    Label(self.frameObjeto, text="P2:").grid(row=4, column=0, sticky=E)
    Label(self.frameObjeto, text="P3:").grid(row=5, column=0, sticky=E)
    Label(self.frameObjeto, text="P4:").grid(row=6, column=0, sticky=E)
    Label(self.frameObjeto, text="P5:").grid(row=7, column=0, sticky=E)
    Label(self.frameObjeto, text="P6:").grid(row=8, column=0, sticky=E)
    Label(self.frameObjeto, text="P7:").grid(row=9, column=0, sticky=E)
    Label(self.frameObjeto, text="P8:").grid(row=10, column=0, sticky=E)
    Label(self.frameObjeto, text="P9:").grid(row=11, column=0, sticky=E)
    Label(self.frameObjeto, text="P10:").grid(row=12, column=0, sticky=E)
    
    #SpinBoxes
    self.spinNVertices = Spinbox(self.frameObjeto, from_=0, to=10, width=7).grid(row=1, column=2, columnspan=2)
    
    #Entradas
    self.entradaA = Entry(self.framePontoVista).grid(row=1, column=1)
    self.entradaB = Entry(self.framePontoVista).grid(row=2, column=1)
    self.entradaC = Entry(self.framePontoVista).grid(row=3, column=1)
    
    self.entradaXPlano = Entry(self.framePlanoProjecao).grid(row=1, column=1)
    self.entradaYPlano = Entry(self.framePlanoProjecao).grid(row=2, column=1)
    self.entradaZPlano = Entry(self.framePlanoProjecao).grid(row=3, column=1)
    
    self.entradasX = [Entry(self.frameObjeto, width=3).grid(row=x+3, column=1) for x in range(10)]
    self.entradasY = [Entry(self.frameObjeto, width=3).grid(row=x+3, column=2) for x in range(10)]
    self.entradasZ = [Entry(self.frameObjeto, width=3).grid(row=x+3, column=3) for x in range(10)]
    
    #Canvas
    self.saidaGrafica = Canvas(self.frameSaidaGrafica, width=640, height=480, bg="white")
    self.saidaGrafica.pack()
    #self.saidaGrafica.create_rectangle(100, 100, 300, 200, activefill="red", width=10)
    
