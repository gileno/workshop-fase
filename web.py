import urllib.request
import json
from pprint import pprint
#
# url = 'https://graph.facebook.com/fmasanori'
# resposta = urllib.request.urlopen(url).read()
# print(resposta)
# dados = json.loads(resposta.decode('utf-8'))
# pprint(dados)
# print('First Name', dados['first_name'])

url = 'https://graph.facebook.com/fmasanori/picture?type=large'
imagem = urllib.request.urlopen(url).read()

arquivo = 'imagem.jpg'
f = open(arquivo, 'wb')
f.write(imagem)
f.close()

print('Imagem salva com sucesso')
