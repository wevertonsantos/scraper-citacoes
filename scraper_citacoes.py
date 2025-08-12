import requests
from bs4 import BeautifulSoup

def main():
    frases = {}

    #buscar dados da página
    dados_pagina = buscar_pagina('https://quotes.toscrape.com/')
    
    # pegando todas as frases
    todas_frases = dados_pagina.find_all('div',class_='quote')

    # percorrendo todas as frases
    for div in todas_frases:
        texto = div.find('span', class_="text").text
        autor = div.find('small', class_="author").text
        frases[autor] = texto

    print(frases)

def buscar_pagina(url):
    try:
        # requisição para página
        pagina = requests.get(url)
        # transformando em html
        dados_pagina = BeautifulSoup(pagina.text,'html.parser')
        return dados_pagina
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar: {e}")

main()