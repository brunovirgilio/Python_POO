import random 
import time

class Luta:
    def __init__(self,n1=0,n2=0 ,p1=0 ,p2=0):
        self.nome1 = n1
        self.nome2 = n2
        self.ponto1 = p1
        self.ponto2 = p2
        
    def definirOponente(self):
        print('''        
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
        ''')        
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
            print(F'\nROUND {r}')
            g1 = int(input('''
            Sua vez de jogar, escolha seu golpe:
            1 - SOCO
            2 - CHUTE
            Digite Aqui>>> '''))
            r = ['ACERTOU','ERROU']
            resultado = random.choice(r)
            if resultado == 'ACERTOU':
                self.ponto1 += 1
            if g1 == 1:
                print(f'\n{self.nome1} aplicou um SOCO e {resultado}')
            else:
                print(f'\n{self.nome1} aplicou um CHUTE e {resultado}')

            print('\nComputador vai jogar...'),time.sleep(4)
            g2 = ['SOCO','CHUTE']
            g3 = random.choice(g2)
            r2 = ['ACERTOU','ERROU']
            resultado2 = random.choice(r2)
            if resultado2 == 'ACERTOU':
                self.ponto2 += 1
            print(f'\n{self.nome2} aplicou um {g3} e {resultado2}')

    def Resultado(self):
        print('\n|','='*50,'|')
        print('|',' '*20,'RESULTADO',' '*19,'|')
        print('|','='*50,'|')
        print(f'|{self.nome1} fez {self.ponto1} ponto(s)|')
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


    



        



"""
class LutadorComputador:
    def __init__(self,*n):
        self.nome = n
        
    def setNome2(self):
        l = ['Jon Jones','George St-Pierre','Chuck Liddell']
        self.nome = random.choice(l)
        print(f' O computador escolheu o {self.nome}.')
        inicio = input('Tecle ENTER para iniciar a luta.')

    def Golpe2(self):
        print('Computador vai jogar...'),time.sleep(4)
        g2 = ['SOCO','CHUTE']
        g3 = random.choice(g2)
        r2 = ['ACERTOU','ERROU']
        resultado2 = random.choice(r2)
        print(f'{self.nome} aplicou um {g3} e {resultado2}')
"""
            




    
    


