# 📘 Books Scraper

Este projeto é um web scraper desenvolvido em Python que utiliza Selenium para extrair informações de livros do site [http://books.toscrape.com/](http://books.toscrape.com/). Os dados coletados são exibidos em uma aplicação web interativa criada com Streamlit, permitindo a filtragem e o download dos dados em formato CSV.

## Funcionalidades

- Raspagem de dados de livros, incluindo título, UPC, preço, disponibilidade, número de reviews, avaliação e URL.
- Navegação automática por todas as páginas do catálogo de livros.
- Interface web com Streamlit para visualização dos dados.
- Filtragem de livros por título.
- Download dos dados coletados em formato CSV.

## Como executar

### 1. Pré-requisitos

- Python 3.7 ou superior
- Google Chrome instalado (o WebDriverManager cuidará do driver correspondente)

### 2. Instalação

Clone este repositório (ou baixe os arquivos):
```bash
# Exemplo, se você for usar git
# git clone <url-do-repositorio>
# cd <nome-do-repositorio>
```

Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- No macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Executando a aplicação

Para iniciar a aplicação Streamlit, execute o seguinte comando no terminal:
```bash
streamlit run main.py
```

A aplicação será aberta automaticamente no seu navegador padrão. Clique no botão "🚀 Iniciar raspagem" para começar o processo de coleta de dados. Após a conclusão, os livros serão exibidos em uma tabela, onde você poderá filtrá-los e baixá-los.

## Estrutura do Projeto

- `main.py`: Contém o código da aplicação Streamlit, interface do usuário e lógica de interação.
- `scraper.py`: Responsável pela lógica de raspagem de dados utilizando Selenium.
- `requirements.txt`: Lista as dependências Python do projeto.
- `README.md`: Este arquivo, fornecendo informações sobre o projeto.
```
