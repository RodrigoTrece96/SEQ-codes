# Datatypes que armazenam várias informações


# BLOCO 1
# Listas: tipo de dados que armazena várias informações e é mutável
# Analogia: a lista é uma grande dispensa que compila vários tipos de informações 
campi_ufrj = []
# campi_ufrj = list()
print(campi_ufrj)

# Adicionando itens à lista que reúne campis da UFRJ
campi_ufrj.append("Fundão")
campi_ufrj.append("Praia Vermelha")
print(campi_ufrj)

# Acessando um item específico da lista:
# A contagem inicia em 0 - a primeira posição é 0
campus_1 = campi_ufrj[0]
print(campus_1)

# Pegando um valor da lista e retirando-a dela - como retirar algo da dispensa
# O método pop, por padrão, pega o último item da lista. Mas é possível especificar a posição, conforme o ex. 
campus = campi_ufrj.pop(0)
print(campus)
print(campi_ufrj)


# BLOCO 2
# Imutabilidade das tuplas e controle das informações armazenadas
campi_ufrj_inalteraveis = ("Fundão", "Praia Vermelha", "Xerém")
print(campi_ufrj_inalteraveis)

# Mostrar que há bem menos métodos para tuplas em comparação a listas e dicts
# campi_ufrj_inalteraveis. 

# Ainda assim é possível acessar informações de tuplas de forma análoga a listas
print(f"Um campus presente na tupla é: {campi_ufrj_inalteraveis[1]}")


# BLOCO 3
# Dicionários: uma forma de associar uma chave a um valor (key-value pair)
materias_departamentos = {"Cálculo II":"IM", "Analexp I":"IQ", "Mecflu":"EQ"} 
print(materias_departamentos)

# Vantagem de usar dicts: dados ficam interligados. Útil quando se deseja conectar informações

# Indexando dicionários - diferenciar de listas e tuplas
# Em dicts, a forma de indexar é através da chave, não pela posição
print(f"Departamento: {materias_departamentos['Cálculo II']}")

# Comentar que possui vários métodos e alguns semelhantes ao de listas: pop(), clear()

# O pop() de dicionários também é um pouco diferente. Ao invés de indexar pela posição, usa-se a chave
# Aqui devolve o valor associado à chave "Mecflu"
print(materias_departamentos.pop("Mecflu"))
