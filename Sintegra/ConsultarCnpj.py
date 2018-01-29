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

#input
input_CNPJ = str(input("insira o cnpj: "))#'07623077000167'
while len(input_CNPJ) != 14:
        print('Verifique o CNPJ digitado!')
        input_CNPJ = str(input("insira o cnpj: "))

formdata['cmbCampo'] = 'CNPJ'
formdata['txtValor'] = input_CNPJ
formdata['B1'] = 'Consultar'


#url inicial de pesquisa + form preenchido
posturl = parse.urljoin(URL, form['action'])


r = s.post(posturl, data=formdata)
resultado = r.content


soup_resultado = BeautifulSoup(resultado, "html.parser")


lista_td = soup_resultado.find('body')
somente_cnpj = soup_resultado.find('body')


dados = []


for texto in lista_td.find_all('td',{'bgcolor': "#FAFAE4"}):
    dados[0] = dados.append(texto.text.replace('\xa0', ''))

cnpj = input_CNPJ


#inicio replaces I E
ie = dados[1].replace('.','')
ie = ie.replace('-','')
ie = ie.replace(' ','')
#fim

razao = dados[2]
ender = dados[3]
num = dados[4]
bairro = dados[5]
cidade = dados[6]

# dados[7] é o estado por extenso
estado = 'CE'

# inicio replaces cep para tirar os pontos
cep = dados[9].replace('.','')
cep = cep.replace('-','')
cep = cep.replace(' ','')
#fim
telefone = dados[10]
situacao = dados[13]
op_simples = dados[22]

_mask_cnpj = (cnpj[0:2]+'.'+cnpj[2:5]+'.'+cnpj[5:8]+'/'+cnpj[8:12]+'-'+cnpj[12:14])
#12.122.518/0001-87 12122518000187






