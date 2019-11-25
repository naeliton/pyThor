import cx_Oracle

#TNSnames.ora

#ORCL =
#  (DESCRIPTION =
#    (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
#    (CONNECT_DATA =
#      (SERVICE_NAME = orcl)
#    )
#  )
# ("Ip_servidor" ,"Porta", "Serviço")

TNS = cx_Oracle.makedsn("187.44.254.2", "1521", "WINT")

con = cx_Oracle.connect(user="MASTERFRIOS", password="M4ST3RFR10S", dsn=TNS)


# print(con.version)
# abre o cursor
class Pesquisa():
    codcli = input(('escolha um codigo'))
    cur = con.cursor()
    cur.prepare('select enderent,numeroent,bairroent,municent,estent,cepent from pcclient where codcli = :codcli')
    cur.execute(None, {'codcli': codcli})
    row = cur.fetchall()[0]
    endereco = row
    print(endereco)
    numero = row[1]
    bairro = row[2]
    cidade = row[3]
    estado = row[4]
    cep = row[4]
    cur.close()
    con.close()
    print('pesquisando')
