import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 100.")

    while True:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if chute == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                break
            elif chute < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

if __name__ == "__main__":
    jogo_adivinhacao()
