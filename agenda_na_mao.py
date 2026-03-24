AGENDA = {
    "gui" : {
        "tel": "99999-1010",
        "email": "gui@gmail.com",
        "endereco": "Av 01",
    } ,
    "maria" : {
        "tel": "98888-1010",
        "email": "maria@gmail.com",
        "endereco": "Av 02",
    } ,
    "joao" : {
        "tel": "97777-1010",
        "email": "joao@gmail.com",
        "endereco": "Av 01",
    } 
}

# print(AGENDA['maria']['tel'])

# ADICIONAR VALOR ISOLADO

# AGENDA['gui']['endereco']="Rua das nações"
# print(AGENDA["gui"])

# ADICIONAR VALORES COMPLETOS

# AGENDA['joao'] = {
#         "tel": "97770-1010",
#         "email": "joao2@gmail.com",
#         "endereco": "Rua 01",
#     } 

# print(AGENDA["joao"])

# REMOVENDO CONTATOS

AGENDA.pop('gui')

print(AGENDA['gui'])