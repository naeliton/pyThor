import cx_Oracle
from pyThor.Sintegra import ConsultarCnpj

# TNSnames.ora

# ORCL =
#  (DESCRIPTION =
#    (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
#    (CONNECT_DATA =
#      (SERVICE_NAME = orcl)
#    )
#  )
# ("Ip_servidor" ,"Porta", "Serviço")

TNS = cx_Oracle.makedsn("host", "port", "service")

con = cx_Oracle.connect(user="user", password="pass", dsn=TNS)


# print(con.version)
# abre o cursor
class Busca():
    cgcent = ConsultarCnpj._mask_cnpj
    cur = con.cursor()
    cur.prepare('select codcli,cliente from pcclient_bkp where cgcent = :cgcent')
    cur.execute(None, {':cgcent': cgcent})
    row = cur.fetchall()
    dados = len(row)
    cur.close()
    con.close()
    #print(dados)





