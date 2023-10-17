import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k = 2.98
tau = 11.925
Theta = 4.925

# Fazendo os cálculos de Kp, Ti, Td usando o método CHR1
kp_chr = 0.30
ti_chr = 11.925
td_chr = 2.46

print('Método de CHR1')
print('Kp = ', kp_chr)
print('Ti = ', ti_chr)
print('Td = ', td_chr, "\n")

# escrevendo a função de transferência da planta
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# Controlador proporcional
numkp = np.array([kp_chr])
denkp = np.array([1])
# integral
numki = np.array([kp_chr])
denki = np.array([ti_chr, 0])

# derivativo
numkd = np.array([kp_chr * td_chr, 0])
denkd = np.array([1])

# Construindo o controlador PID
Hkp = cnt.tf(numkp, denkp)
Hki = cnt.tf(numki, denki)
Hkd = cnt.tf(numkd, denkd)
Hctrl1 = cnt.parallel(Hkp, Hki)
Hctrl = cnt.parallel(Hctrl1, Hkd)
Hdel = cnt.series(Hs, Hctrl)

# Fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)

t = np.linspace(0, 140, 100)
(t, y) = cnt.step_response(2*Hcl, t)

# Fazendo os cálculos de Kp, Ti, Td usando o método CC
kp_cc = 0.27
ti_cc = 10.42
td_cc = 1.67


print('Método de Cohen e Coon')
print('Kp = ', kp_cc)
print('Ti = ', ti_cc)
print('Td = ', td_cc)

# escrevendo a função de transferência da planta
num_cc = np.array([k])
den_cc = np.array([tau, 1])
H_cc = cnt.tf(num_cc, den_cc)
n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs_cc = cnt.series(H_cc, H_pade)

# Controlador proporcional
numkp_cc = np.array([kp_cc])
denkp_cc = np.array([1])
# integral
numki_cc = np.array([kp_cc])
denki_cc = np.array([ti_cc, 0])

# derivativo
numkd_cc = np.array([kp_cc * td_cc, 0])
denkd_cc = np.array([1])

# Construindo o controlador PID
Hkp_cc = cnt.tf(numkp_cc, denkp_cc)
Hki_cc = cnt.tf(numki_cc, denki_cc)
Hkd_cc = cnt.tf(numkd_cc, denkd_cc)
Hctrl1 = cnt.parallel(Hkp_cc, Hki_cc)
Hctrl_cc = cnt.parallel(Hctrl1, Hkd_cc)
Hdel_cc = cnt.series(Hs_cc, Hctrl_cc)

# Fazendo a realimentação
Hcl_cc = cnt.feedback(Hdel_cc, 1)

t = np.linspace(0, 150, 100)
(t, y1) = cnt.step_response(2*Hcl_cc, t)

plt.plot(t, y, label='CHR1 - Método Clássico')
plt.plot(t, y1, label='CC - Método Novo')

plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')
plt.title('Controle PID')

plt.grid()
plt.show()
#