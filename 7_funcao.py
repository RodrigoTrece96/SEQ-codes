# Funções em Python: uma forma de organizar o código e reutilizar blocos importantes que performam uma ação


# BLOCO 1
# Estrutura de uma função em Python: palavras-chave "def" e "return"
# Falar sobre "side effects" e uma boa prática de *retornar* algo em funções ao invés de somente *printar*

def minha_info():
    nome = input("Digite seu nome: ").lower().title().strip() # Comentar sobre outros str methods: strip() e title()
    curso = input("Digite seu curso: ").lower().title().strip()

    return f"Meu nome é {nome} e estou estudando {curso}"


print(minha_info())


# BLOCO 2
# Usando funções para quebrar o problema em etapas menores e juntar os bloquinhos no final
# Problema: avaliar se o email do usuário é da UFRJ

def main(): 
    email = email_usuario()
    print(email)


def email_usuario():
    while True:
        email = input("Digite seu email UFRJ: ").strip()

        if email.endswith("ufrj.br"):
            return email
        else:
            print("Email UFRJ inválido")
            continue 


main()
