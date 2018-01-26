import cx_Oracle
import geoPEsquisa
import geopyWin

TNS = cx_Oracle.makedsn("192.168.0.3", "1521", "WINT")
con = cx_Oracle.connect(user="dsl", password="dsl", dsn=TNS)
print('validando informaçoes')
latitude = geoPEsquisa.latitude
longitude = geoPEsquisa.longitude
codcli = geopyWin.Pesquisa.codcli

cur = con.cursor()
statement = 'update pcclient_bkp set latitude = :latitude, longitude =:longitude where codcli = :codcli'
print('Aplicando atualização')
cur.execute(statement, (latitude,longitude, codcli))
con.commit()
cur.close()
con.close()
print('Number of rows updated: ' + str(cur.rowcount))
print(' ')




