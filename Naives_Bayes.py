#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
#Ambiente
AsolS = 0
AnubS = 0
AllovS = 0
#Temperatura
TAltS = 0
TMedS = 0
TBajS = 0
#Humedad
HAltS = 0
HNorS = 0
#Viento
VsS = 0
VnS = 0

#Ambiente
AsolN = 0
AnubN = 0
AllovN = 0
#Temperatura
TAltN = 0
TMedN = 0
TBajN = 0
#Humedad
HAltN = 0
HNorN = 0
#Viento
VsN = 0
VnN = 0

#-------Resultados------- 

solS = 0
solN = 0
nubS = 0
nubN = 0
lluvS = 0
lluvN = 0

#------Temperatura-------

AltS = 0
AltN = 0
MedS = 0
MedN = 0
BajS = 0
BajN = 0

#----Humedad-----------

HaS = 0
HaN = 0
HnS = 0
HnN = 0

#-------Viento---------

Vss = 0
Vns = 0
Vsn = 0
Vnn = 0

data = pd.read_csv('Datos_naives_bayes.csv')
print(data)


# %%
clase = data['clase']
viento = data['viento']
hum = data['humedad']
temp = data['temperatura']
amb = data['ambiente']
# %%
si=np.where(data.clase==1)[0]
no = np.where(data.clase==2)[0]
# %%
PclaseS = len(si)/len(data)
PclaseN = len(no)/len(data)
# %%
#-----VALORES POSITIVOS------
#----Ambiente-----
for i in si:
    #ambiente
    if data['ambiente'].loc[i] == 1:
        AsolS += 1
    if data['ambiente'].loc[i] == 2:
        AnubS += 1
    if data['ambiente'].loc[i] == 3:
        AllovS += 1
    #Temperatura
    if data['temperatura'].loc[i] == 1:
        TBajS += 1
    if data['temperatura'].loc[i] == 2:
        TMedS += 1
    if data['temperatura'].loc[i] == 3:
        TAltS += 1
    #Humedad
    if data['humedad'].loc[i] == 1:
        HAltS += 1
    if data['humedad'].loc[i] == 2:
        HNorS += 1
    #Viento
    if data['viento'].loc[i] == 1:
        VsS += 1
    if data['viento'].loc[i] == 1:
        VnS += 1
    
# %%
#-----VALORES NEGATIVOS------
for i in no:
    #ambiente
    if data['ambiente'].loc[i] == 1:
        AsolN += 1
    if data['ambiente'].loc[i] == 2:
        AnubN += 1
    if data['ambiente'].loc[i] == 3:
        AllovN += 1
    #Temperatura
    if data['temperatura'].loc[i] == 1:
        TBajN += 1
    if data['temperatura'].loc[i] == 2:
        TMedN += 1
    if data['temperatura'].loc[i] == 3:
        TAltN += 1
    #Humedad
    if data['humedad'].loc[i] == 1:
        HAltN += 1
    if data['humedad'].loc[i] == 2:
        HNorN += 1
    #Viento
    if data['viento'].loc[i] == 1:
        VsN += 1
    if data['viento'].loc[i] == 1:
        VnN += 1
    
#%%
#------CALCULO PROB---------
#-------Ambiente----------
solS = AsolS/len(si)
solN = AsolN/len(no)
nubS = AnubS/len(si)
nubN = AnubN/len(no)
lluvS = AllovS/len(si)
lluvN = AllovN/len(no)
#-------Temperatura---------
AltS = TAltS/len(si)
AltN = TAltN/len(no)
MedS = TMedS/len(si)
MedS = TMedN/len(no)
BajS = TBajS/len(si)
BajN = TBajN/len(no)
#--------Humedad------------
HaS = HAltS/len(si)
HaN = HAltN/len(no)
HnS = HNorS/len(si)
HnN = HNorN/len(no)
#--------Viento-------------
Vss = VsS/len(si)
Vns = VsN/len(no)
Vsn = VnS/len(si)
Vnn = VnN/len(no)

#%%
#-----------Datos a Evaluar---------




# %%
