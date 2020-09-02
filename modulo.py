import random 
import time

class Lutador:
    def __init__(self,*n):
        self.nome = n
        
    def setNome(self):
        j1=int(input(''' \tUFC PYTHON\n
        Escolha seu lutador: 
        1 - Anderson Silva
        2 - José Aldo
        3 - Junior Cigano
        Digite Aqui>>> '''))
        if j1 == 1:
            self.nome = 'Anderson Silva'    
        elif j1 == 2:
            self.nome = 'José Aldo'
            
        elif j1 == 3:
            self.nome = 'Junior Cigano'

        print(f' Seu lutador é {self.nome}.')

    def setNome2(self):
        l = ['Jon Jones','George St-Pierre','Chuck Liddell']
        self.nome = random.choice(l)
        print(f' O computador escolheu o {self.nome}.')
        inicio = input('Tecle ENTER para iniciar a luta.')

    def Luta(self):
        r = ['ACERTOU','ERROU']
        resultado = random.choice(r)
        golpe = int(input('''
        Sua vez de jogar, escolha seu golpe:
        1 - soco
        2 - chute
        Digite Aqui>>> '''))
        if golpe == 1:
            print(f'{self.nome} aplicou um SOCO e {resultado}')
        else:
            print(f'{self.nome} aplicou um CHUTE e {resultado}')

    def Luta2(self):
        print('Computador vai jogar...'),time.sleep(4)
        g2 = ['SOCO','CHUTE']
        golpe2 = random.choice(g2)
        r2 = ['ACERTOU','ERROU']
        resultado2 = random.choice(r2)
        print(f'{self.nome} aplicou um {golpe2} e {resultado2}')

            




    
    


