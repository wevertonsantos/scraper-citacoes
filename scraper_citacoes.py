import requests
from bs4 import BeautifulSoup
from translate import Translator
translator = Translator(to_lang="pt")

def main():
    frases = {}

    #buscar dados da página
    dados_pagina = buscar_pagina('https://quotes.toscrape.com/')
    
    # pegando todas as frases
    todas_frases = dados_pagina.find_all('div',class_='quote')

    frases_no_dicionario(todas_frases,frases)

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

def frases_no_dicionario(todas_frases,frases):
    # percorrendo todas as frases
    for div in todas_frases:
        # pegando texto
        texto_ingles = div.find('span', class_="text").text
        # traduzindo texto inglês para português
        texto_portugues = translator.translate(texto_ingles)
        # pegando autor
        autor = div.find('small', class_="author").text
        # adicionando texto e autor no dicionário
        frases[autor] = texto_portugues

main()