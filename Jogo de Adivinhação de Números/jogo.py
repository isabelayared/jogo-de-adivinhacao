import random

def jogar(nivel_dificuldade):
    tentativas = 0
    acertou = False

    if nivel_dificuldade == 1:
        numero_secreto = random.randint(1, 50)
        print("Tente adivinhar o número entre 1 e 50.")
    elif nivel_dificuldade == 2:
        numero_secreto = random.randint(1, 100)
        print("Tente adivinhar o número entre 1 e 100.")
    elif nivel_dificuldade == 3:
        numero_secreto = random.randint(1, 200)
        print("Tente adivinhar o número entre 1 e 200.")
    else:
        print("Opção inválida. Configurando nível Médio.")
        numero_secreto = random.randint(1, 100)
        nivel_dificuldade = 2  

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            if palpite < numero_secreto:
                print("O número secreto é maior!")
            elif palpite > numero_secreto:
                print("O número secreto é menor!")
            else:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                acertou = True
        except ValueError:
            print("Por favor, insira um número válido.")

def selecionar_dificuldade():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Selecione o nível de dificuldade:")
    print("1. Fácil (1-50)")
    print("2. Médio (1-100)")
    print("3. Difícil (1-200)")

    try:
        escolha = int(input("Escolha 1, 2 ou 3: "))
        jogar(escolha)
    except ValueError:
        print("Opção inválida. Tente novamente.")
        selecionar_dificuldade()

selecionar_dificuldade() 
