# Loops tem a função de reiterar uma ação no código. 
# Ao invés de manualmente escrever várias linhas de código com a mesma essência, pode-se usar um loop


# BLOCO 1
# Dois tipos de loop: for e while

# Exemplo de for para gerar informações através do range
# Mostrar que esse loop economiza linhas de código e o flexibiliza 
for i in range(10):
    print(i)

# Insight interessante do for: ele é exclusivo. Então o 10 não aparece, vai de 0 a 9

# Falar um pouco de escopo e da notação += 
i = 0
while i != 10:
    print(i)
    i += 1 


# BLOCO 2
# Iterando sobre dicionários - um exemplinho para unir os conceitos 
materias_departamentos = {"Cálculo II":"IM", "Analexp I":"IQ", "Mecflu":"EQ"} 

for materias in materias_departamentos:
    print(materias_departamentos[materias])

departamentos = []
for materias in materias_departamentos:
    departamentos.append(materias_departamentos[materias])

# Apresentando a função sorted nativa do Python. Por default organiza em ordem alfabética ou crescente
print(departamentos)
print(sorted(departamentos))    
print(*sorted(departamentos))


# BLOCO 3
# Loops infinitos e break: o break é uma forma de sair de um loop

# Uma lista de supermercado

checklist_mercado = []

print("Caso a lista esteja completa, digite: Concluído")

while True:    
    item = input("Digite o que você deseja adicionar à lista: ").lower().capitalize()

    if item == "Concluído":
        break 
    else:
        checklist_mercado.append(item)

print(checklist_mercado)
