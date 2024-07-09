import random
def jogar():
    posibilidades = ['pedra','papel','tesoura']

    acertou = 0
    errou = 0
    empate = 0

    while True:
        escolha = input('Escolha  (pedra), (papel) ou (tesoura), pra cancelar o jogo, escreva (sair): \n')
        pc = random.choice(posibilidades)    
        if escolha == 'sair':
            print(f'Jogo acabou. Seu placar foi de {acertou} e a maquinan fez {errou}')
            break
        elif escolha not in posibilidades:
            print('Não é uma escolha possivel ')
            continue

        if escolha == pc:
            print('--Empate --') 
            empate += 1

        elif (escolha == 'pedra' and pc == 'tesoura') or \
             (escolha == 'papel' and pc == 'pedra') or \
             (escolha == 'tesoura' and pc == 'papel'):
            print('--Ganhou--') 
            acertou+= 1
        
        else:
            print('Derrota ')
            errou+= 1

jogar()



