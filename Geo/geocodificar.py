import googlemaps
import oracle

API_Key = 'AIzaSyBvRhvRYNv0iI-OM0UJ70DIOnmjlsQm4Ks'

gm = googlemaps.Client(key=API_Key)

def  googlecodificar(codcli,endereco):


  geocode_result = gm.geocode(endereco)
  if len(geocode_result) == 0:
      print('Cliente não localizado '+str(codcli))
      return 1
  else:
      geocode_result= geocode_result[0]
      latitude = geocode_result['geometry']['location']['lat']
      longitude = geocode_result['geometry']['location']['lng']
      oracle.Updatecodificao(codcli,latitude,longitude)
      return 0
