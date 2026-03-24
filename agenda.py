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
     
def excluir_contato(contato):
    AGENDA.pop(contato)
    print('>>>> Contato {} excluído com sucesso'.format(contato))

def imprimir_menu():
    print('''
        1 - Mostrar todos os contatos da agenda
        2 - Buscar contato
        3 - Adicionar contato
        4 - Editar contato
        5 - Excluir contato
        0 - Fechar agenda 
        '''
    )

imprimir_menu()

# sempre que sai do INPUT sai como STRING
opcao = input('Escolha uma opção:')

if opcao == '1':
     mostrar_contatos()
elif opcao == '2':
     contato = input('Digite o nome do contato:')
     buscar_contato(contato)
elif opcao == '3' or opcao == '4':
     nome = input('Digite o nome:')
     telefone = input('Digite o telefone:')
     email = input('Digite o email:')
     endereco = input('Digite o endereço:')
     incluir_editar_contato(nome, telefone, email, endereco)
elif opcao == '5':
     contato = input('Digite o nome do contato:')
     excluir_contato(contato)
elif opcao == '0':
     exit
else:
     print('Opção inválida.')

