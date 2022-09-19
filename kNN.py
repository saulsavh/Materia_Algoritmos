
#* vecinos mas cercanos
#? ALgoritmo
#? Fase 1: Fase de aprendizaje donde almacena todos los vectores de carracteristicas
#?         Asocia una clase a cada vector del conjunto de aprendizaje
#! Fase 2: Fase de clasificacion, dentro de un ciclo for se calcula la distancia Euclidiana entre Y y X^k
#!         Con la formula pow(sum(xi-yi)^2)
#todo      Determina las distancias mas cercanas entre Y y X^k 
#todo      de las distancias mas cercanas y dado el valor k, selecciona la clase pertenecientes de los vectores 
#todo      Selecciona la clase que mas se repite

#%%
#* Inicio de codigo
import collections
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




#%%
#? fase dos, creamos clase para calcular las distancias
class knn (object):
    def __init__(self,k, df,c):
        self.k = k
        self.df = df
        self.c = c
        self.label=self.df['Marca']
    
    @classmethod
    def datos (cls):
        distancia = pd.DataFrame(columns=['Distancias'])
        for i in cls.df:
            valor = knn.cal_dist(c[0], c[1], cls.df['Animes Vistos'][i], cls.df['Tiempo años'][i])
            distancia.append(valor)
    
    @classmethod
    def cal_dist (cls,x,y,x1,y1):
        return np.sqrt(((x-x1)**2)+((y-y1)**2))
    
    @classmethod
    def resultado (cls):
        return cls.distancia



#%%
#* Fase 1 cargar dataset
k=1
data = pd.read_csv('datos.csv')
x = data['Animes Vistos']
y = data['Tiempo años']
c = np.array([20,4])


#%%
#* visualizacion de data
plt.figure(1)
plt.title('Eres otaku?')
plt.xlabel('Animes Vistos')
plt.ylabel('Años')
plt.plot((x.head(5)),(y.head(5)),'ro')
plt.plot(x.tail(),y.tail(),'bs')
plt.plot(c[0],c[1],'^g')
plt.show()
# %%

otaku =knn(k,data,c)