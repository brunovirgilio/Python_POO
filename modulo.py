import random 
import time

class Luta:
    def __init__(self,n1=0,n2=0 ,p1=0 ,p2=0):
        self.nome1 = n1
        self.nome2 = n2
        self.ponto1 = p1
        self.ponto2 = p2
        
    def definirOponente(self):
        print('''\033[1;31m        
        -------------------------------------------------        
        -------------------------------------------------        
        -----+++---+++---++++++++++++------+++++---------
        -----+++---+++---++++++++++++---+++++++++++------
        -----+++---+++---++++----------++++-----++++-----
        -----+++---+++---+++++++-----++++----------------
        -----+++---+++---+++++++-----++++----------------
        -----+++---+++---++++----------++++-----++++-----
        -----+++++++++---++++-----------+++++++++++------
        -----+++++++++---++++--------------+++++---------
        -------------------------------------------------
        -------------------------------------------------
        \033[m''')        
        j1=int(input('''\n
        Escolha seu lutador: 
        1 - ANDERSON SILVA
        2 - JOSÉ ALDO
        3 - JUNIOR CIGANO
        Digite Aqui>>> '''))
        if j1 == 1:
            self.nome1 = 'ANDERSON SILVA'    
        elif j1 == 2:
            self.nome1 = 'JOSÉ ALDO'            
        elif j1 == 3:
            self.nome1 = 'JUNIOR CIGANO'

        print(f'\nSeu lutador é {self.nome1}.')

        l = ['JON JONES','GEORGE ST-PIERRE','CHUCK LIDDELL']
        self.nome2 = random.choice(l)
        print(f'\nO computador escolheu o {self.nome2}.')
        inicio = input('\nTecle ENTER para iniciar a luta.')

    def IniciarLuta(self):
        for r in range(1,6):
            print(f'\n\033[1;33mROUND {r}\033[m')
            g1 = int(input('''
            Sua vez de jogar, escolha seu golpe:
            1 - SOCO
            2 - CHUTE
            Digite Aqui>>> '''))
            r = ['\033[1;32mACERTOU\033[m','\033[1;31mERROU\033[m']
            resultado = random.choice(r)
            if resultado == '\033[1;32mACERTOU\033[m':
                self.ponto1 += 1
            if g1 == 1:
                print(f'\n{self.nome1} aplicou um SOCO e {resultado}')
            else:
                print(f'\n{self.nome1} aplicou um CHUTE e {resultado}')

            print('\nComputador vai jogar...'),time.sleep(4)
            g2 = ['SOCO','CHUTE']
            g3 = random.choice(g2)
            r2 = ['\033[1;32mACERTOU\033[m','\033[1;31mERROU\033[m']
            resultado2 = random.choice(r2)
            if resultado2 == '\033[1;32mACERTOU\033[m':
                self.ponto2 += 1
            print(f'\n{self.nome2} aplicou um {g3} e {resultado2}')

    def Resultado(self):
        print('\n|','='*50,'|')
        print('|',' '*20,'RESULTADO',' '*19,'|')
        print('|','='*50,'|')
        '''print(f'|{self.nome1} fez {self.ponto1} ponto(s)|')'''
        print('|',' '*20,f'{self.nome1} fez {self.ponto1} ponto(s)',' '*19,'|')
        print (f'|{self.nome2} fez {self.ponto2} ponto(s)|')
        print('|','='*50,'|')
        if self.ponto1 > self.ponto2:
            print(f'|{self.nome1} GANHOU|')
            print('|','='*50,'|')
        elif self.ponto1 < self.ponto2:
            print(f'|{self.nome2} GANHOU|')
            print('|','='*50,'|')
        else:
            print('|A luta foi EMPATADA|')
            print('|','='*50,'|')




    
    


