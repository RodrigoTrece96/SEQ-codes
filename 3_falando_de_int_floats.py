# Apresentando inteiros e distinção com strings


# BLOCO 1
x = input("Digite um número: ")
y = input("Digite um número: ")

# Outra forma de concatenar strings 
soma = x + y 
print(f"Soma = {soma}")
print(type(soma))

# Não adiciona os espaços: soma substrings em strings maiores 
print("engenharia" + "química")


# BLOCO 2
x = int(input("Digite um número: "))
y = int(input("Digite um número: "))

soma = x + y 
print(f"Soma = {soma}")
print(type(soma))


# BLOCO 3
# Aplicando os operadores e usando Python para fazer contas 
# Falar um pouco de floats 
distancia = float(input("Digite a distância percorrida (metros): "))
velocidade = float(input("Informe a velocidade média do trajeto (m/s): "))

tempo = distancia/velocidade
print("O tempo do percurso foi", tempo)

# Convertendo unidades e arredondando com a função round
tempo_min = round(tempo/60, 2)
print(tempo_min)


# BLOCO 4
# Calculando a altura através da fórmula da queda livre
### Inicialmente, não converter para float as variáveis: interagir com o pessoal
velocidade_inicial = float(input("Velocidade inicial da queda: "))
gravidade = float(input("Gravidade: "))
tempo_queda = float(input("Tempo de queda: "))
altura = velocidade_inicial*tempo + 1/2*gravidade*tempo_queda**2

print(f"A altura da queda é {altura}")
