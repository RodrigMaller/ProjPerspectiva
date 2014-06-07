from Tkinter import *

class App:
  
  def __init__(self, master):
    #init Frames
    self.framePontoVista = Frame(master, relief=FLAT, borderwidth=2)
    self.framePlanoProjecao = Frame(master, relief=FLAT, borderwidth=2)
    self.frameSaidaGrafica = Frame(master, relief=SUNKEN, borderwidth=2)
    
    #Griding Frames
    self.framePontoVista.grid(row=0, column=0)
    self.framePlanoProjecao.grid(row=1, column=0)
    self.frameSaidaGrafica.grid(row=0, column=1, rowspan=2)
    
    #Labels
    Label(self.framePontoVista, text="Ponto de Vista").grid(row=0, column=0, columnspan=2)
    Label(self.framePontoVista, text="A:").grid(row=1, column=0, sticky=E)
    Label(self.framePontoVista, text="B:").grid(row=2, column=0, sticky=E)
    Label(self.framePontoVista, text="C:").grid(row=3, column=0, sticky=E)
    
    Label(self.framePlanoProjecao, text="Plano de Projecao:").grid(row=0, column=0, columnspan=2)
    Label(self.framePlanoProjecao, text="X:").grid(row=1, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="Y:").grid(row=2, column=0, sticky=E)
    Label(self.framePlanoProjecao, text="Z:").grid(row=3, column=0, sticky=E)
    
    #Entradas
    self.entradaA = Entry(self.framePontoVista).grid(row=1, column=1)
    self.entradaB = Entry(self.framePontoVista).grid(row=2, column=1)
    self.entradaC = Entry(self.framePontoVista).grid(row=3, column=1)
    
    self.entradaXPlano = Entry(self.framePlanoProjecao).grid(row=1, column=1)
    self.entradaYPlano = Entry(self.framePlanoProjecao).grid(row=2, column=1)
    self.entradaZPlano = Entry(self.framePlanoProjecao).grid(row=3, column=1)
    
    #Canvas
    self.saidaGrafica = Canvas(self.frameSaidaGrafica, width=480, height=320)
    self.saidaGrafica.pack()
    self.saidaGrafica.create_rectangle(100, 100, 300, 200, activefill="red", width=10)
    
