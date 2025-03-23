# Bibliotecas: chegando ao final dos primeiros passos
# Elas são usadas para não ter que reinventar a roda e utilizar de conceitos que outros programadores já enfrentaram 


# BLOCO 1 
# Exemplo de biblioteca nativa do Python. Não precisa usar pip
import random


def main():
    resposta = escolher_numero()
    print(avaliar_chute(resposta))


def escolher_numero():
    primeiro_numero = int(input("Digite o menor número para o intervalo de adivinhação: "))
    ultimo_numero = int(input("Digite o último número para o intervalo de adivinhação: "))
    
    resposta = random.randint(primeiro_numero, ultimo_numero)

    return resposta


def avaliar_chute(numero):
    while True:
        chute = int(input("Digite seu palpite: "))

        if chute == numero:
            return "Você acertou!!!"

        elif chute < numero:
            print("Muito pequeno!")
        
        elif chute > numero:
            print("Muito grande!")


if __name__ == "__main__":
    main()
