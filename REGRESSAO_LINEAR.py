import pandas as pd
import math as mt
import matplotlib.pyplot as plt
import numpy as np

# Vetores 1/T e ln(K)

it = [] #Inverso da temperatura
lnk = [] #Logarítmo natural de K


# Leitura do banco de dados

x = pd.read_excel(r"C:\Users\Carlos Filho\Desktop\DADOS_REGRESSAO.xlsx")
tamanho = len (x["T"])


#Convertendo T e K para plotar os pontos na regressão

for i in range(tamanho):
    ti = (x ["T"] [i])
    tik = ti+273.15
    invt = 1/tik
    it.append(invt)
    ki = (x ["k"] [i])
    kiln = mt.log(ki)
    lnk.append(kiln)

plt.scatter (it,lnk)
plt.grid
plt.xlabel("1/T")
plt.ylabel("ln k")
plt.show


# Regressão Linear

media_X = np.mean(it)
media_Y = np.mean(lnk)
erro_x = it-media_X
erro_y = lnk-media_Y
soma_erro_xy = np.sum(erro_x*erro_y)
erro_x_quadratico = (it-media_X)**2
soma_erro_x_quadratico = np.sum(erro_x_quadratico)


# Coeficientes da regressão

m = soma_erro_xy / soma_erro_x_quadratico
print("Coeficiente angular = {:0.2f}".format(m))

c = media_Y - m*media_X
print("Coeficiente linear = {:0.2f}".format(c))


# Exibição gráfica da Regressão Linear

X = x ['T'].values
Xi = 1/(X+273.15)

plt.scatter(it,lnk)
plt.plot(it, (m*Xi+c) ,label='Ajuste linear',color='green')
plt.xlabel('1/T')
plt.ylabel('ln k')