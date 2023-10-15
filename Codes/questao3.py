import numpy as np
import control as cnt
import matplotlib.pyplot as plt

from scipy.io import loadmat

mat=loadmat('TransferFunction2.mat')
degrau = mat.get('degrau')
saida=mat.get('saida')
t1 = mat.get('t')

k = 2.98
tau = 11.925
Theta = 4.925 

num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)
t = np . linspace (0 ,70, 100)

# Vamos multiplicar Hs por 2, pq é o valor do degrau
(t , y ) = cnt.step_response ( 2*Hs, t )
plt.plot(t, y, label='Saida Estimada')
plt.plot (t1.T, saida, label='Saida Original' )

# Degrau
# plt.plot (t , y1, label='Degrau de Entrada' )

plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')

plt.legend(loc='lower right')
plt.title('Função de saida Original x Estimada')
plt.grid ()
plt.show()