conjunto_cores = {"vermelho", "azul", "verde"}

# não adiciona elementos repetidos (até deixa, mas filtra)

conjunto_cores.add("branco")
conjunto_cores.add("branco")

print(conjunto_cores)

conjunto_cores.remove("branco")

print(conjunto_cores)
