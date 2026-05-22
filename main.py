import pandas as pd

caminho = r"C:\Users\renan\OneDrive\Área de Trabalho\Projeto Automação\planilha_teste\Base.xlsx"

ler = pd.read_excel(caminho)


def ped_entregues():
    pedidos_entregues = ler.loc[
        ler['Status'] == 'Entregue',
        ['Data','Pedido','Cliente','Produto','Categoria','Cidade','Status','Valor']
    ]

    return pedidos_entregues

def ped_cancelados():
    pedidos_cancelados = ler.loc[
        ler['Status'] == 'Cancelado',
        ['Data', 'Pedido', 'Cliente', 'Produto', 'Categoria', 'Cidade', 'Status', 'Valor']
    ]

    return pedidos_cancelados

def exportar():
    print("""Digite o que você quer exportar
    [1] - Exportar somente pedidos entregues
    [2] - Exportar somente pedidos cancelados""")

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        arquivo = ped_entregues()
        nome_arquivo = 'Pedidos_entregues.xlsx'
        arquivo.to_excel(nome_arquivo, index = False)

        print('Exportação concluída')

    elif escolha == 2:
        arquivo = ped_cancelados()
        nome_arquivo = 'Pedidos_cancelados.xlsx'
        arquivo.to_excel(nome_arquivo, index = False)

        print('Exportação concluída')

while True:
    print("""Bem-vindo à minha automação
    [1] - Listar pedidos entregues
    [2] - Listar pedidos cancelados
    [3] - Exportar informações""")
    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        print(ped_entregues())
    elif escolha == 2:
        print(ped_cancelados())
    elif escolha == 3:
        exportar()