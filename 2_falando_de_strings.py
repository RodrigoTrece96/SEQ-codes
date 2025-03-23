# BLOCO 1 
# Strings possuem vários métodos, mas são imutáveis: é possível fazer alterações e armazenas as alterações
# mas a string inicial permanece igual ao início

nome = "helena"

# Mostrar a documentação com os métodos de strings
nome_formatado = nome.capitalize()

# Mostrando que strings são imutáveis
print(f"Antigo: {nome} // Novo: {nome_formatado}")


# BLOCO 2 
# Formatando o input do usuário
nome_usuario = input("Digite seu nome: ")

# Mostrar o input desformatado 
print(nome_usuario)

# O método lower padroniza todas as letras, depois o capitalize deixa só a primeira maiúscula  
nome_usuario = nome_usuario.lower().capitalize()
print(nome_usuario)

# Pode-se economizar linhas de código
print(nome_usuario.lower().capitalize())
