# Calcular o volume de um gás ideal através da fórmula V = nRT/p


# Quebrando o problema em pedaços menores 
# Uma função *lambda* é usada e *exceptions*: et cetera
def main():
    pressao, temperatura, moles = pegar_variaveis()
    v = lambda p, t, n: n*0.082*t/p  # V = n.R.T/p

    volume = v(pressao, temperatura, moles)

    print(volume)


def pegar_variaveis():
    while True:
        try:
            pressao = float(input("Digite a pressão em atm: "))
            temperatura = float(input("Digite a temperatura em graus K: "))
            moles = float(input("Digite o número de moles do gás: "))
        except ValueError:
            print("Os valores digitados devem ser números")
        else:
            if temperatura >= 0 and pressao >= 0 and moles >= 0:            
                    return pressao, temperatura, moles
        
            print("Os parâmetros não possuem sentido físico")


if __name__ == "__main__":
    main()
