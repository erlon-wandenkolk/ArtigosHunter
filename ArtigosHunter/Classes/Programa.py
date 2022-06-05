from Classes.Artigo import Artigo
import time
import os
from Classes.setup import ROOT_DIR,BASE_DIR

class Programa:

    def __init__(self):
        pass

    def cadastrar_artigo(self, titulo='', categoria='', data='', texto=''):
        artigo = Artigo(titulo, categoria, data, texto)
        self.__salvar_artigo__(artigo)
        self.__criar_indice__(artigo)
        self.__indexar_base__()

    def __salvar_artigo__(self, artigo):
        caminho = os.path.join(ROOT_DIR+os.sep+'Biblioteca'+os.sep+artigo.assunto+os.sep+artigo.nome_arquivo)
        with open(caminho, 'w') as arquivo:
            arquivo.write('Titulo: ' + artigo.titulo + '\n')
            arquivo.write('\n')
            arquivo.write(
                'Assunto: ' + artigo.assunto + '          DATA:' + artigo.data_publicacao.strftime("%Y_%m_%d"))
            arquivo.write('\n')
            arquivo.write('\n')
            arquivo.write(artigo.texto_original)

        print('Artigo salvo com sucesso!')
        time.sleep(1)

    def __criar_indice__(self, artigo):
        indice_artigo = f'{artigo.data_publicacao};{artigo.titulo};{artigo.assunto};{artigo.nome_arquivo};{artigo.palavras_unicas};{artigo.total_unicas}\n'
        # sumario = 'DATA_PUBLICACAO;TITULO;ASSUNTO;NOME_DO_ARQUIVO;LISTA_PALAVRAS_UNICAS;TOTAL_PALAVRAS_UNICAS'

        with open(BASE_DIR, 'a') as arquivo:
            arquivo.write(indice_artigo)

    def __indexar_base__(self):

        with open(BASE_DIR, 'r') as arquivo:
            arquivo = arquivo.readlines()
            lista = [i for i in arquivo]
        lista.sort()

        with open(BASE_DIR, 'w') as arquivo:
            arquivo.writelines(lista)

    def gerar_relatorio_similaridade(self):
        lista = []
        with open(BASE_DIR, 'r') as arquivo:
            arquivo = arquivo.readlines()
            lista = [i.replace('\n', '').split(';') for i in arquivo]

        comparacoes = []

        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                comparacoes.append(self.__calcular_relatorio__(lista[i], lista[j]))

        self.__imprimir_relatorio__(comparacoes)

    def __imprimir_relatorio__(self, comparacoes):
        comparacoes.sort(reverse=True)
        for i in comparacoes:
            print(f'\t{i[1]:30} \t--- e ---\t {i[2]:30}\t--- possuem similidade de\t {round(i[0], 2)}%')

    def __calcular_relatorio__(self, artigo_a, artigo_b):
        palavras_unicas_a = artigo_a[4][2:-2].replace("'", '').strip().split(',')
        palavras_unicas_b = artigo_b[4][2:-2].replace("'", '').strip().split(',')
        matchs = 0
        for i in palavras_unicas_a:
            if i in palavras_unicas_b:
                matchs += 1
        coeficiente = 100 * matchs / (float(artigo_a[-1]) + float(artigo_b[-1]))
        return [coeficiente, artigo_a[1], artigo_b[1], matchs]

    def __consultar_artigos__(self):
        with open(BASE_DIR, 'r') as arquivo:
            arquivo = arquivo.readlines()
            lista = [i.replace('\n', '').split(';') for i in arquivo]
        print(f'\t N -- \tDATA PUBICACAO\t      NOME DO ARTIGO\t                   CATEGORIA \t                          NOME DO ARQUIVO')
        n=1
        for artigo in lista:
            print(f'\t {n}N -- \t{artigo[0]:12} -- \t{artigo[1]:30} -- \t{artigo[2]:30} -- \t{artigo[3]}')
            n += 1
        opcao = int(input('Digite o número do arquivo que deseja ler, ou 0 para fechar: '))
        if opcao != 0:
            assunto = lista[opcao - 1][2]
            nome_arquivo = lista[opcao - 1][3]
            return assunto, nome_arquivo
        else:
            return 0, 0

    def __abrir_artigo__ (self,assunto,nome_artigo):
        caminho = os.path.join(ROOT_DIR + os.sep + 'Biblioteca' + os.sep + assunto + os.sep + nome_artigo)
        with open(caminho) as arquivo:
            print(arquivo.read())