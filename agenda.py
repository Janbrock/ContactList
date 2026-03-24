AGENDA = {}

AGENDA['Guilherme'] = {
    'telefone': '99999-9999',
    'email': 'guilherme@python.com.br',
    'endereco': 'Av. 1'
}

AGENDA['Maria'] = {
    'telefone': '99999-9998',
    'email': 'maria@python.com.br',
    'endereco': 'Av. 2'
}

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('------------------')

def buscar_contato(contato):
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco
    }
    print('>>>> Contato {} adicionado/editado com sucesso'.format(contato))
     

mostrar_contatos()
incluir_editar_contato('Joana', '988887777', 'joana@python.com.br', 'Av. 3')
incluir_editar_contato('Guilherme', '988886666', 'joana@python.com.br', 'Av. 3')
incluir_editar_contato('José', '988885555', ' ', None)
mostrar_contatos()