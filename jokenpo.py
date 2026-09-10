#1ª atividade: Adicionar 3 chances para jogar (repetir o jogo 3x)

import random

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura"]

for i in range(3):

    jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: ").capitalize())

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")
    elif jogador == "Pedra":
        if pc == "Tesoura":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Papel":
        if pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

print("Obrigada por jogar!")
   