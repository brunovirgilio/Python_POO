import random 

class Lutador:
    def __init__(self,*n):
        self.nome = n
        
    def setNome(self):
        j1=int(input(''' \tUFC PYTHON\n
        1 - Anderson Silva
        2 - José Aldo
        3 - Junior Cigano
        Escolha seu lutador: '''))
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

    def luta(self):
        inicio = input('Tecle ENTER para iniciar a luta.')
        while True:
            g = ['soco','chute']
            print('''
            Sua vez de jogar, escolha seu golpe:
            1 - soco
            2 - chute''')
            random.choice(g)




    
    


