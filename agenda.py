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
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>> Agenda vazia.')    

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print()
    except KeyError:
        print('>>>> Contato inexistente.')
    except Exception as error:
        print('Um erro inesperado ocorreu!')
        print(error)

def incluir_editar_contato(contato):
        telefone = input('Digite o telefone:')
        email = input('Digite o email:')
        endereco = input('Digite o endereço:')

        AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
        }
     
def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print()
        print('>>>> Contato {} excluído com sucesso'.format(contato))
        print()
    except KeyError:
        print('>>>> Contato inexistente.')
    except Exception as error:
        print('Um erro inesperado ocorreu!')
        print(error)

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

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção:')

    if opcao == '1': # mostrar
        print('''
              LISTA DE CONTATOS
              ''')
        mostrar_contatos()
    elif opcao == '2': # buscar
        contato = input('Digite o nome do contato:')
        buscar_contato(contato)
    elif opcao == '3': # adicionar
        contato = input('Digite o nome:')
        try:
            AGENDA[contato]
            print()
            print('>>>> Contato já existe.')
        except:
            incluir_editar_contato(contato)
            print()
            print('>>>> Contato {} adicionado com sucesso.'.format(contato))
    elif opcao == '4': # editar
        contato = input('Digite o nome:')
        try:
            AGENDA[contato]
            incluir_editar_contato(contato)
            print()
            print('>>>> Contato {} editado com sucesso.'.format(contato))
        except KeyError:
            print()
            print('>>>> Contato inexistente.')
            
    elif opcao == '5': # excluir
        contato = input('Digite o nome do contato:')
        excluir_contato(contato)
    elif opcao == '0': # fechar
        print('>>>> Fechando o programa...')
        break
    else:
        print()
        print('>>>> Opção inválida.')
        print()

