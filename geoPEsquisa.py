import googlemaps
from geopyWin import Pesquisa

API_Key = 'AIzaSyBvRhvRYNv0iI-OM0UJ70DIOnmjlsQm4Ks'

gm = googlemaps.Client(key=API_Key)


endereco = Pesquisa.endereco

#RUA, numero ,Bairro,cidade ,Estado,cep
endereco = (endereco)


geocode_result = gm.geocode(endereco)[0]

latitude = geocode_result['geometry']['location']['lat']

longitude = geocode_result['geometry']['location']['lng']


print('Latitude e longitude')
print(latitude, longitude)
print('Endereço')
print(endereco)



