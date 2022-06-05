from Classes.Programa import Programa

class Interface:
    def __init__(self):
        pass

    def menu(self):
        desligar = False
        programa = Programa()
        while not desligar:
            print("----- BEM VINDO AO ARTIGOS HUNTER --------")
            print('Digite a opção desejada:')
            print('1- Cadastrar Artigo.')
            print('2 - Ver relatorio de similaridade.')
            print('3 - Excluir artigo da base.')
            print('4 - Consultar artigos.')
            print('0 - Finalizar o Programa.')
            opcao = input(' ___ -> ')
            if opcao == '1':
                print('Iniciando cadastro!')
                titulo = input('Digite o titulo do artigo: ').title()
                categoria = input('Digite a categoria do artigo: ').title()
                data = input('Digite a data no formato AAAA/MM/DD: ')
                texto = input('Digite o conteúdo/texto do artigo: ')
                programa.cadastrar_artigo(titulo,categoria,data,texto)
            elif opcao =='2':
                programa.gerar_relatorio_similaridade()
            elif opcao =='3':
                print('Opção em Desenvolvimento')
            elif opcao =='4':
                assunto, nome_artigo = programa.__consultar_artigos__()
                if assunto != 0:
                    programa.__abrir_artigo__(assunto,nome_artigo)
            elif opcao =='0':
                print('Finalizando o Programa')
                desligar = True
                print('Programa Finalizado')
            else:
                print('Opção Inválida. Tente novamente')
