#2ª atividade: Mudar a estrutura do jogo adicionando mais opções
import random

print("Jogo Jokenpo!")

opcoes = ["Pedra", "Papel", "Tesoura", "Bota", "Fogo"]

while True:
    jogador = str(input("Escolha entre Pedra, Papel, Tesoura, Bota ou Fogo : ").capitalize())

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
        if pc == "Pedra"or pc == "Bota":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel" or pc == "Bota":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Bota":
            if pc == "Papel" or pc == "Pedra":
                print("Você venceu!")
            else:
                print("O seu adversario venceu!")
    elif jogador == "Fogo":
                if pc == "Bota" or pc == "Papel" or pc == "Tesoura":
                    print("Você venceu!")
                else:
                    print("O seu adversario venceu!")


    restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
    if restart != "SIM":
        break