import random

print("Jogo de Adivinhação")

opcoes = [1,2,3,4,5,6,7,8,9,10]

for i in range(3):
    print("Você tem 3 chances para acertar o número")
    jogador = int(input("Escolha um número de 1 a 10: "))
    

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.randint(1,10)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Você adivinhou o número!!")
        break
    else:
            print("Não foi dessa vez")
print("Jogue novamente")