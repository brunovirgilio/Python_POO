import random 
import time

class Lutador:
    def __init__(self,n1=0,n2=0 ,p1=0 ,p2=0):
        self.nome1 = n1
        self.nome2 = n2
        self.ponto1 = p1
        self.ponto2 = p2
        
    def setNome(self):
        j1=int(input(''' \t
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
        \n
        Escolha seu lutador: 
        1 - Anderson Silva
        2 - José Aldo
        3 - Junior Cigano
        Digite Aqui>>> '''))
        if j1 == 1:
            self.nome1 = 'Anderson Silva'    
        elif j1 == 2:
            self.nome1 = 'José Aldo'
            
        elif j1 == 3:
            self.nome1 = 'Junior Cigano'

        print(f' Seu lutador é {self.nome1}.')

    def setNome2(self):
        l = ['Jon Jones','George St-Pierre','Chuck Liddell']
        self.nome2 = random.choice(l)
        print(f' O computador escolheu o {self.nome2}.')
        inicio = input('Tecle ENTER para iniciar a luta.')

    def Golpe1(self):
        g1 = int(input('''
        Sua vez de jogar, escolha seu golpe:
        1 - soco
        2 - chute
        Digite Aqui>>> '''))
        r = ['ACERTOU','ERROU']
        resultado = random.choice(r)
        if resultado == 'ACERTOU':
            self.ponto1 += 1
        if g1 == 1:
            print(f'{self.nome1} aplicou um SOCO e {resultado}')
        else:
            print(f'{self.nome1} aplicou um CHUTE e {resultado}')

    def Golpe2(self):
        print('Computador vai jogar...'),time.sleep(4)
        g2 = ['SOCO','CHUTE']
        g3 = random.choice(g2)
        r2 = ['ACERTOU','ERROU']
        resultado2 = random.choice(r2)
        if resultado2 == 'ACERTOU':
            self.ponto2 += 1
        print(f'{self.nome2} aplicou um {g3} e {resultado2}')

    def Final(self):
        print (f'{self.nome1} fez {self.ponto1} ponto(s).')
        print (f'{self.nome2} fez {self.ponto2} ponto(s).')

        if self.ponto1 > self.ponto2:
            print(f'{self.nome1} GANHOU.')
        elif self.ponto1 < self.ponto2:
            print(f'{self.nome2} GANHOU.')
        else:
            print('A luta foi EMPATADA')


    



        



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
            




    
    


