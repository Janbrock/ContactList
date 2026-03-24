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

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('------------------')

def buscar_contato(contato):
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])

mostrar_contatos()
# buscar_contato('maria')