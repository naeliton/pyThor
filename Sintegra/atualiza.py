from pyThor.Sintegra.conexao import *

cadastrado = Busca.dados


if (cadastrado == 1):
    row = Busca.row[0]
    codcli = row[0]
    print('Cliente cadastrado no codigo {}'.format(codcli))
elif(cadastrado == 0):
    print('Cliente não cadastrado')
else:
    print('contate o Desenvolvedor!')