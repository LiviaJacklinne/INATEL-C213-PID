import numpy as np
import control as cnt
import matplotlib.pyplot as plt

class CC:

    def calc_cc():
        # considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
        k = 2.98
        tau = 11.925
        Theta = 4.925

        # Fazendo os cálculos de Kp, Ti, Td usando o método CC
        kp_cc = 1.16
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

        t = np.linspace(50, 90, 100)
        (t, y) = cnt.step_response(2*Hcl_cc, t)
        plt.plot(t, y)
        plt.xlabel(' t [ s ] ')
        plt.ylabel('Amplitude')
        plt.legend(loc='lower right')
        plt.title('Controle PID - Método Novo CC')

        plt.grid()
        plt.show()
