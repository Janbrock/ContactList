AGENDA = {}

# CRIANDO UM AAGENDA NA MÃO

AGENDA['guilherme'] = {
    'telefone': '99999-9999',
    'email': 'guilherme@python.com.br',
    'endereco': 'Av. 1'
}

AGENDA['maria'] = {
    'telefone': '99999-9998',
    'email': 'maria@python.com.br',
    'endereco': 'Av. 2'
}

# DEF = DEFINIR
# PASS = PASSA
# CRIANDO MÉTODO PARA MOSTRAR CONTATOS

def mostrar_contato():
    for contato in AGENDA:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('------------------')

# mostrar_contato()

def buscar_contato(contato):
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])

buscar_contato('maria')