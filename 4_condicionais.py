# Condicionais e Booleanos no controle do fluxo do código


# BLOCO 1 
# Booleanos: True ou False - duas possibilidades 
# Condicionais: if, elif, else

# Aqui só printa os booleanos. A seguir eles serão usados para manipular o fluxo do código
print("1 > 2", 1 > 2)
print("1 = 1", 1 == 1)   
print("2 > 1", 2 > 1) 


# BLOCO 2
# Avaliando a absorbância através de condicionais
absorbância = float(input("Digite a absorbância medida: "))

# Forma Pythônica de escrever
# if 0 <= absorbância <= 1:
#     print("Tem sentido físico")

if absorbância >= 0 and absorbância <= 1:
    print("Tem sentido físico")
else:
    print("Não tem sentido físico, pois essa grandeza varia de 0 a 1")


# BLOCO 3
# Avaliando se o aluno foi aprovado 
nota_p1 = float(input("Nota da P1: "))
nota_p2 = float(input("Nota da P2: "))

media = (nota_p1 + nota_p2)/2

if media >= 7:
    print(f"Aprovado direto com média {media}")
elif 3 <= media < 7:
    print(f"Prova final com média {media}")
elif media < 3:
    print(f"Reprovado com média {media}")
