import cx_Oracle
from pyThor.Geo import pesquisa
from pyThor.Geo import conecta

TNS = cx_Oracle.makedsn("host", "port", "service")

con = cx_Oracle.connect(user="user", password="pass", dsn=TNS)
latitude = pesquisa.latitude
longitude = pesquisa.longitude
codcli = conecta.Pesquisa.codcli

cur = con.cursor()
statement = 'update pcclient_bkp set latitude = :latitude, longitude =:longitude where codcli = :codcli'
cur.execute(statement, (latitude, longitude, codcli))
con.commit()
cur.close()
con.close()
print('Número de linhas atualizadas: ' + str(cur.rowcount))
print(' ')




