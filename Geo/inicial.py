import oracle

entrada =input(('Escolha uma opção: \n 1-atualizar todos os código nulo \n 2-atualizar um código especifico\n'))

if entrada == '1':
    print('Atualizar tudos')
    oracle.Atualizartodos()
elif entrada == '2':
    print('Atualizar um código')
    codcli = input(('Dígite código\n'))
    oracle.AtualizarCodigo(codcli)
else:
    print('Escolha Errada!')
