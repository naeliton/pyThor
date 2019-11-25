import cx_Oracle
import geocodificar

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





def Updatecodificao(codcli,latitude,longitude):
    cur = con.cursor()
    statement = 'update pcclient set latitude = :latitude, longitude =:longitude where codcli = :codcli'
    cur.execute(statement, (latitude, longitude, codcli))
    con.commit()



def Atualizartodos():
    cur = con.cursor()
    count= 0
    for row in cur.execute('select codcli,enderent,numeroent,bairroent,municent,estent,cepent from pcclient where latitude is null or longitude is null'):
        codcli = row[0]
        endereco = row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]
        if geocodificar.googlecodificar(codcli,endereco) == 0 :
           count = count+1


    print('Total de linhas atualizadas: '+str(count))

def AtualizarCodigo(codcli):
     cur = con.cursor()
     cur.prepare('select enderent,numeroent,bairroent,municent,estent,cepent from pcclient where codcli = :codcli')
     cur.execute(None, {'codcli': codcli})
     row = cur.fetchall()[0]
     endereco = row
     geocodificar.googlecodificar(codcli,endereco)
     print('Geolocalização do cliente '+codcli+' foi atualizada!')
