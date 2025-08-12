import requests
from bs4 import BeautifulSoup


# requisição para página
pagina = requests.get('https://quotes.toscrape.com/')
# transformando em um html
dados_pagina = BeautifulSoup(pagina.text,'html.parser')
# melhorando estrutura html da página
print(dados_pagina.prettify())

def main():
    ...

def pagina():
    ...    

main()