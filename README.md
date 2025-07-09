# 📘 Books Scraper

Este projeto é um web scraper desenvolvido em Python que utiliza Selenium para extrair informações de livros do site [books.toscrape.com](http://books.toscrape.com/). Os dados coletados são exibidos em uma aplicação web interativa criada com Streamlit, permitindo a filtragem e o download dos dados em formato CSV.

## Funcionalidades

- Coleta de dados de livros, incluindo título, UPC, preço, disponibilidade, número de reviews, avaliação e URL.
- Navegação automática por todas as páginas do catálogo de livros.
- Interface web interativa com Streamlit para visualização e filtragem dos dados.
- Filtragem de livros por título.
- Download dos dados coletados em formato CSV.

## Tecnologias Utilizadas

- Python
- Selenium (para web scraping)
- Streamlit (para a interface web)
- Pandas (para manipulação de dados)
- WebDriver Manager (para gerenciamento automático do ChromeDriver)

## Como executar

### 1. Pré-requisitos

- Python 3.7 ou superior.
- Google Chrome instalado. (O WebDriverManager cuidará da instalação do ChromeDriver correspondente).

### 2. Instalação

Primeiro, obtenha os arquivos do projeto. Você pode clonar o repositório se tiver Git instalado:
```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```
Ou baixe os arquivos `.zip` e extraia-os.

Crie um ambiente virtual (altamente recomendado para isolar as dependências do projeto):
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

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Executando a Aplicação

Para iniciar a aplicação Streamlit, execute o seguinte comando no terminal, na pasta raiz do projeto:
```bash
streamlit run main.py
```

A aplicação será aberta automaticamente no seu navegador padrão. Clique no botão "🚀 Iniciar raspagem" para começar o processo de coleta de dados. Após a conclusão, os livros serão exibidos em uma tabela, onde você poderá filtrá-los por título e realizar o download dos dados em formato CSV.

## Estrutura do Projeto

- `main.py`: Contém o código da aplicação Streamlit, responsável pela interface do usuário e lógica de interação.
- `scraper.py`: Módulo responsável pela lógica de raspagem de dados (web scraping) utilizando Selenium.
- `requirements.txt`: Lista todas as dependências Python necessárias para o projeto.
- `.gitignore`: Especifica arquivos e pastas que devem ser ignorados pelo Git.
- `books_scraper.log`: Arquivo de log gerado pela execução do scraper (configurado em `scraper.py`). Recomenda-se adicionar este arquivo ao `.gitignore`.
- `README.md`: Este arquivo, fornecendo informações sobre o projeto.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes (se aplicável, ou defina uma licença).
(Nota: Adicionar um arquivo LICENSE se desejar formalizar a licença)
```
