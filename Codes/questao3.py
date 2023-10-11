import numpy as np
import control as cnt
import matplotlib.pyplot as plt

'''
Função de malha aberta, segundo os valores de K, THETA e TAU que achamos 
pelo metodo SMITH

'''
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
'''
Ajustes finos 
k = 2.97 >> 2.84
tau = 3.13
Theta = 0.63 >> 0.65 # atraso de propagação
'''

k = 2.84
tau = 3.13
Theta = 0.65

num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)
# Hmf = cnt.feedback(Hs, 1)

t = np . linspace (0 ,40, 100)

# Vamos multiplicar Hs e Hmf por 2, pq é o valor do degrau
(t , y ) = cnt.step_response ( 2*Hs, t )
# (t , y1 ) = cnt.step_response ( 2*Hmf, t)

plot1 = plt.plot (t , y, label='Saida' )
# plot2 = plt.plot (t , y1, label='Degrau de Entrada' )
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')

plt.title('Função Estimada')
plt.grid ()
plt.show()