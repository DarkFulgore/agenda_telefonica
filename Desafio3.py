#####Catálogo telefônico#####

catalogo = {}  ##Criada dicionário


def incluir():

def pesquisar():

def listar():

def apagar():

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

while True:   ##Enquanto a entrada for verdadeira, será executado o loop
    opcao = menu_principal()
    if opcao == 5:  ##realizado o break quando o usuário digitar a opção "5: sair"
        break
    elif opcao == 1:
        incluir()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        listar()
    elif opcao == 4:
        apagar()
    else:          ##utilizei mais uma condição para informar para o usuário que o mesmo digitou uma opção errada
        print("*" * 50)
        print(f'{"OPÇÃO ERRADA!!!!!!":^50}')
        print(f'{"INFORME UMA OPÇÃO VÁLIDA":^50}')
        print("*" * 50)






