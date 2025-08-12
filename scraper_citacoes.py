import requests
from bs4 import BeautifulSoup


# requisição para página
pagina = requests.get('https://quotes.toscrape.com/')
# transformando em um html
dados_pagina = BeautifulSoup(pagina.text,'html.parser')
# melhorando estrutura html da página
# print(dados_pagina.prettify())

# pegando todas as frases
todas_frases = dados_pagina.find_all('div',class_='quote')

# percorrendo todas as frases
for div in todas_frases:
    print(div)

def main():
    ...

def pagina():
    ...    

main()