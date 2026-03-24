# Podem ser criadas com ou sem parênteses

# cores = "amarelo", "azul", "roxo"
tupla_cores = ("amarelo", "azul", "roxo")
lista_cores = ["amarelo", "azul", "roxo"]

lista_cores[1] = "branco"

# Tuplas não adicionam elementos (imutáveis)
# tupla_cores[1] = "branco" 

# aceitam iterações
for cor in tupla_cores:
    print(cor)

# print(tupla_cores)
# print(lista_cores)