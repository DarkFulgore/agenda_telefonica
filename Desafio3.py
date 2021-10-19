#####Catálogo telefônico#####

catalogo = []  ##Criada Lista


def menu_principal():   ##Função que exibe o Menu Principal do Catálogo
    print('-' * 50)
    print(f'{"MENU PRINCIPAL - CATÁLOGO TELEFÔNICO":^50}')
    print('-' * 50)
    print(f'{"1: Incluir novo contato":<50}')
    print(f'{"2: Pesquisar um contato":<50}')
    print(f'{"3: Mostrar toda a lista de contatos":<50}')
    print(f'{"4: Apagar um contato":<50}')
    print(f'{"5: Sair":<50}')
    print('-' * 50)
    validar = float(input('Informe sua opção: '))   ##Input da opção informada pelo usuário/convertido para float
    return validar

###Escopo das chamadas do menu principal
while True:   ##Enquanto a entrada for verdadeira, será executado o loop
    opcao = menu_principal()
    if opcao == 5:  ##realizado o break quando o usuário digitar a opção "5: sair"
        break
    elif opcao == 1:   ###Cadastro de nome e telefone
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        contato = {'nome': nome, 'telefone': telefone}  ##criado um dicionário para armazenar nome e telefone
        catalogo.append((contato))  ##o dicionario é adicionado ao final da lista
        print(f'{nome} foi adicionado.')  ##imprimindo o nome do contato
    elif opcao == 2:
        nome = input("Informe o nome que deseja buscar: ")
        contato_encontrado = False
        for contato in catalogo:
            if contato['nome'] == nome:
                print(f'Nome: {contato["nome"]}')
                print(f'Telefone: {contato["telefone"]}')
                contato_encontrado = True
                break
        if contato_encontrado == False:
            print('Nome não foi encontrado')
    elif opcao == 3:   ###Mostra toda a lista de Contatos
        print('\nLISTA DE CONTATOS')
        for contato in catalogo:        ##fazendo uma busca em toda a lista
            print(f'Nome: {contato["nome"]}')  ##imprime o valor da chave nome do dicionario inserido na lista
            print(f'Telefone: {contato["telefone"]}')  ##imprime o valor da chave telefone do dicionario inserido na lista
    elif opcao == 4:  ###Remover um contato pelo nome
        nome = input("Digite o nome do contato que deseja remover: ")  ##entrada do nome que deseja apagar
        contato_encontrado = False
        for contato in catalogo:    ##fazendo a busca do nome informado na lista
            if contato['nome'] == nome:   ##caso o nome informado seja igual ao encontrado na lista
                catalogo.remove(contato)  ##função para remover um elemento da lista
                print(f'{nome} foi removido')
                contato_encontrado = True ##para não ter que listar todos os elementos após a operação ser efetuada, utiliza o op booleano True
                break    ##usa-se o break para finalizar a condição
        if contato_encontrado == False:   ##caso a condição continue o operador False, imprime a msg de não encontrado
            print('Nome não foi encontrado')
    else:          ##utilizei mais uma condição para informar para o usuário que o mesmo digitou uma opção errada
        print("*" * 50)
        print(f'{"OPÇÃO ERRADA!!!!!!":^50}')
        print(f'{"INFORME UMA OPÇÃO VÁLIDA":^50}')
        print("*" * 50)






