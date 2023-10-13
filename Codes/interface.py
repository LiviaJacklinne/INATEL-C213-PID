import numpy as np
import control as cnt
import matplotlib.pyplot as plt

from questao5_CC import *
from questao5_CHR import *

k = 2.98
tau = 11.925
Theta = 4.925 

def PID():
    print('Insira agora os dados dos parâmetros PID')
    kp = float(input('Kp = '))
    ti = float(input('Ti = '))
    td = float(input('Td = '))
    degrau = float(input('Degrau = '))
    print('')

    # escrevendo a função de transferência da planta
    num = np.array([k])
    den = np.array([tau, 1])
    H = cnt.tf(num, den)
    n_pade = 20
    (num_pade, den_pade) = cnt.pade(Theta, n_pade)
    H_pade = cnt.tf(num_pade, den_pade)
    Hs = cnt.series(H, H_pade)

    # Controlador proporcional
    numkp = np.array([kp])
    denkp = np.array([1])
    # integral
    numki = np.array([kp])
    denki = np.array([ti, 0])

    # derivativo
    numkd = np.array([kp * td, 0])
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

    t = np.linspace(0, 40, 100)
    (t, y) = cnt.step_response(degrau * Hcl, t)
    plt.plot(t, y)
    plt.xlabel(' t [ s ] ')
    plt.ylabel('Amplitude')
    plt.title('Controle PID')

    plt.grid()
    plt.show()

flag = True
while flag:
    print('----------------------------------')
    print('0 - Sair')
    print('1 - Ver PID com CHR1')
    print('2 - Ver PID com CC')
    print('3 - Calcular PID manualmente')

    menu = int(input('O que deseja fazer: '))
    print('')

    if(menu == 0):
        flag = False

    elif(menu == 1):
        CHR1.calc_chr()

    elif(menu == 2):
        CC.calc_cc()

    elif(menu == 3):
        PID()
    else:
        print('Valor inválido! Tente novamente.')