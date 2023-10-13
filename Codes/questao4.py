import numpy as np
import control as cnt
import matplotlib.pyplot as plt

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
Hmf = cnt.feedback(Hs, 1)
t = np . linspace (0 ,40, 100)

# Vamos multiplicar Hs e Hmf por 2, pq é o valor do degrau
(t , y ) = cnt.step_response ( 2*Hs, t )
plt.plot(t, y, label='Malha Aberta')

(t , y1 ) = cnt.step_response ( 2*Hmf, t)
plt.plot(t, y1, label='Malha Fechada')

plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')

plt.title('Malha Aberta x Malha Fechada')
plt.grid ()
plt.show()

#