#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import *
import requests
from urllib import parse

URL = 'http://www.sefaz.ce.gov.br/content/aplicacao/internet/servicos_online/sintegra/sintegra.asp?estado=ce'
s = requests.Session()


def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content


soup = BeautifulSoup(fetch(URL), "html.parser")
form = soup.find('form')
fields = form.findAll('input')

formdata = dict((field.get('name'), field.get('value')) for field in fields)

formdata['cmbCampo'] = 'CNPJ'
formdata['txtValor'] = '07623077000167'
formdata['B1'] = 'Consultar'

# print (formdata)

posturl = parse.urljoin(URL, form['action'])

# print(posturl)

r = s.post(posturl, data=formdata)
resultado = r.content

soup_resultado = BeautifulSoup(resultado, "html.parser")
##tras o <body > da pagina total
lista_td = soup_resultado.find('body')
#texto = soup_resultado.find_all('td')

texto_td = {}

#texto1 = lista_td.find_all('td',{'bgcolor':"#FAFAE4",'width':'36%'})
#lista somente onte no body tem um td com 'bgcolor'= "#FAFAE4", 'width'= "36%"

for texto in lista_td.find_all('td',{'bgcolor': "#FAFAE4", 'width': "36%"}):
    #texto_td[texto.text] = texto.text
    texto_td[texto.text] = texto.text.replace('\xa0', '').strip()

print(texto_td.values())