import numpy as np 
import math

class Complejo():
    def __init__(self,r, i):
        self.imaginario= i
        self.real=r
        return self.imaginario
        return self.real
    def conjugado(self,r,i):
        self.imaginario = (-1)*i
        return self.imaginario 
    def calcula_norma():
        self.norma = (r**2+i**2)**(1/2)
        return self.norma
    def pow(self,i,p):
        self.imaginario= i**p
        return self.imaginario
