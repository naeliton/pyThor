import cx_Oracle
from pyThor.Geo import pesquisa
from pyThor.Geo import conecta

TNS = cx_Oracle.makedsn("187.44.254.2", "1521", "WINT")

con = cx_Oracle.connect(user="MASTERFRIOS", password="M4ST3RFR10S", dsn=TNS)
latitude = pesquisa.latitude
longitude = pesquisa.longitude
codcli = conecta.Pesquisa.codcli

cur = con.cursor()
statement = 'update pcclient set latitude = :latitude, longitude =:longitude where codcli = :codcli'
cur.execute(statement, (latitude, longitude, codcli))
con.commit()
cur.close()
con.close()
print('Número de linhas atualizadas: ' + str(cur.rowcount))
print(' ')
