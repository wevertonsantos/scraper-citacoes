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

    # colocando frases no dicionário
    frases_no_dicionario(todas_frases,frases)

    salvando_arquivo(frases)

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

def salvando_arquivo(frases):
    with open("Citações.txt",'w') as arquivo:
        for frase in frases:
            if list(frases.keys())[-1]:
                arquivo.write(f"{frase}:{frases[frase]}")
        else:
            arquivo.write(f"{frase}:{frases[frase]}\n\n")

main()