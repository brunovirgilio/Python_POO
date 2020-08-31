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

class Luta:
    def __init__(self,*j1,*j2):
        self.lutador1 = j1
        self.lutador2 = j2
    
    


