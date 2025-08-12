# 📝 Web Scraper de Citações com Tradução

Este projeto é um **web scraper** que coleta frases do site [Quotes to Scrape](https://quotes.toscrape.com/), traduz automaticamente para o português e salva todas as citações junto com seus autores em um arquivo `.txt`.

## 🚀 Funcionalidades

- **Coleta automática** de citações no site.
- **Tradução automática** do inglês para português usando a biblioteca `translate`.
- **Armazenamento** das citações em um arquivo de texto chamado `Citações.txt`.
- **Associação autor ↔ frase** no formato:
  ```
  Autor: Frase traduzida
  ```

## 🛠 Tecnologias usadas

- [Python 3.x](https://www.python.org/)
- [Requests](https://pypi.org/project/requests/) – para fazer requisições HTTP.
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – para analisar e extrair dados do HTML.
- [Translate](https://pypi.org/project/translate/) – para traduzir as frases.

## 📦 Instalação

1. **Clone este repositório**.
2. **Instale as dependências** com:
   ```bash
   pip install requests beautifulsoup4 translate
   ```

## ▶️ Como executar

No terminal, navegue até a pasta do projeto e execute:

```bash
python scraper_citacoes.py
```

Após a execução, será criado o arquivo `Citações.txt` na mesma pasta do script.

## 📫 Contato
Se quiser falar comigo sobre o projeto ou oportunidades:
- 💼 [LinkedIn](https://linkedin.com/in/wevertonsantoss)
- 📧 wevercanal@gmail.com