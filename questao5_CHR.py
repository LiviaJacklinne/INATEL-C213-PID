import numpy as np
import control as cnt
import matplotlib.pyplot as plt

class CHR1: 
    def calc_chr():
        # considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
        k = 2.84
        tau = 3.13
        Theta = 0.65

        # Fazendo os cálculos de Kp, Ti, Td usando o método CHR1
        kp_chr = 0.994
        ti_chr = 3.135
        td_chr = 0.3175

        print('Kp calculado por ZN = ', kp_chr)
        print('Ti calculado por ZN = ', ti_chr)
        print('Td calculado por ZN = ', td_chr)

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

        t = np.linspace(50, 90, 100)
        (t, y) = cnt.step_response(2*Hcl, t)
        plt.plot(t, y)
        plt.xlabel(' t [ s ] ')
        plt.ylabel('Amplitude')
        plt.legend(loc='upper right')
        plt.title('Controle PID - Método Clássico CHR1')

        plt.grid()
        plt.show()