from modulo import Luta


r = 'S'
while not r == 'N':
    l1 = Luta()
    l1.definirOponente()
    l1.IniciarLuta()
    l1.Resultado()
    r = input('DESEJA REPETIR O JOGO? [S] ou [N]: ').upper()
    if r == 'N':
        print('='*10)
        print('GAME OVER')
        print('='*10)
