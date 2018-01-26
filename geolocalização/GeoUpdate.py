import cx_Oracle
from pyThorGeo.geolocalização import geoPEsquisa
from pyThorGeo.geolocalização import geopyWin

TNS = cx_Oracle.makedsn("localhost", "1521", "orcl")
con = cx_Oracle.connect(user="dsl", password="dsl", dsn=TNS)
latitude = geoPEsquisa.latitude
longitude = geoPEsquisa.longitude
codcli = geopyWin.Pesquisa.codcli

cur = con.cursor()
statement = 'update pcclient_bkp set latitude = :latitude, longitude =:longitude where codcli = :codcli'
cur.execute(statement, (latitude, longitude, codcli))
con.commit()
cur.close()
con.close()
print('Número de linhas atualizadas: ' + str(cur.rowcount))
print(' ')




