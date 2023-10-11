from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt


'''
O professor passou uma função de transferencia com valores pré-definidos por ele.
Apenas para tirarmos as informações de K, THETA e TAU.

Usando o método de SMITH achamos:
K = 2.98 (ganho, vPico/degrau)
tau = 3.135
theta = 0.635 (atraso, tempo que a função demorou para começar a subir)
'''

# Carregando função de transferencia
mat=loadmat('TransferFunction2.mat')

#Variáveis
degrau = mat.get('degrau')
saida=mat.get('saida')
t1 = mat.get('t')


plot1=plt.plot(t1.T,saida, label='Saída')
plot2=plt.plot(t1.T,degrau,label='Degrau de Entrada')
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")

plt.title('Função Original')
plt.grid ()
plt.show()