import menu_nav
import Tela
executar = True
while executar: 
    Tela.LimpaTela()
    print('Seja bem vindo ao Organico’s 🙂.\nAqui você pode comprar nossos produtos direto pelo seu celular!')
    red = int(input('Digite o número de uma das opções abaixo: \n 1 - Menu de Navegação \n 2 - Encerrar o programa. \n'))
    while red not in range(1, 3):
        print('Por favor, digite o valor 1 ou 2.')
        red = int(input())
    if red == 1:
        print('Que bom que está continuando com a gente! Você está sendo redirecionada (o) para o nosso menu de navegação!')
        menu_nav.nav()
    elif red == 2:
        executar = False
        print('Obrigada por visitar nosso programa. Volte sempre!')