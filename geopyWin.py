import cx_Oracle

TNS = cx_Oracle.makedsn("192.168.0.3", "1521", "WINT")

con = cx_Oracle.connect(user="dsl", password="dsl", dsn=TNS)
#print(con.version)
#abre o cursor
class Pesquisa():
    codcli = input(('escolha um codigo'))
    cur = con.cursor()
    cur.prepare('select enderent,numeroent,bairroent,municent,estent,cepent from pcclient_bkp where codcli = :codcli')
    cur.execute(None, {'codcli': codcli})
    row = cur.fetchall()[0]
    endereco = row
    numero = row[1]
    bairro = row[2]
    cidade = row[3]
    estado = row[4]
    cep = row[4]
    cur.close()
    con.close()
    print('pesquisando')


