from typing import Optional
import pandas as pd
from selenium.webdriver.chrome.webdriver import WebDriver
import logging

# Configuração de logging para arquivo
logging.basicConfig(
    filename="books_scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    encoding="utf-8"
)


def criar_driver() -> WebDriver:
    """
    Cria e configura um driver Chrome headless para Selenium usando webdriver_manager.

    Returns:
        WebDriver: Instância do Chrome WebDriver configurado.
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    logging.info("Driver Chrome criado com sucesso.")
    return driver


def raspar_livros(driver: WebDriver, base_url: Optional[str] = "http://books.toscrape.com/") -> pd.DataFrame:
    """
    Raspagem completa do site 'Books to Scrape', coletando dados de todas as páginas.

    Args:
        driver (WebDriver): Instância do Selenium WebDriver configurado.
        base_url (str, opcional): URL inicial para começar a raspagem. Default é 'http://books.toscrape.com/'.

    Returns:
        pd.DataFrame: DataFrame contendo informações detalhadas dos livros coletados.
    """
    import time
    from selenium.webdriver.common.by import By

    driver.get(base_url)
    time.sleep(1)
    livros = []
    livro_count = 0

    while True:
        links = driver.find_elements(By.CSS_SELECTOR, "h3 a")
        total_links = len(links)
        print(f"Iniciando página com {total_links} livros...")
        logging.info(f"Iniciando nova página com {total_links} livros.")

        for i in range(total_links):
            links = driver.find_elements(By.CSS_SELECTOR, "h3 a")
            link = links[i]
            url = link.get_attribute("href")
            link.click()
            time.sleep(0.3)

            livro_count += 1
            print(f"Lendo livro {livro_count}: {url}")
            logging.info(f"Lendo livro {livro_count}: {url}")

            try:
                dados = {
                    "Title": driver.find_element(By.CSS_SELECTOR, "h1").text,
                    "UPC": driver.find_element(By.XPATH, '//th[contains(text(), "UPC")]/following-sibling::td').text,
                    "Product Type": driver.find_element(By.XPATH, '//th[contains(text(), "Product Type")]/following-sibling::td').text,
                    "Price (excl. tax)": driver.find_element(By.XPATH, '//th[contains(text(), "Price (excl. tax)")]/following-sibling::td').text,
                    "Price (incl. tax)": driver.find_element(By.XPATH, '//th[contains(text(), "Price (incl. tax)")]/following-sibling::td').text,
                    "Tax": driver.find_element(By.XPATH, '//th[contains(text(), "Tax")]/following-sibling::td').text,
                    "Availability": driver.find_element(By.XPATH, '//th[contains(text(), "Availability")]/following-sibling::td').text,
                    "Number of reviews": driver.find_element(By.XPATH, '//th[contains(text(), "Number of reviews")]/following-sibling::td').text,
                    "Rating": driver.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split(" ")[1],
                    "URL": url,
                }
                livros.append(dados)
                logging.info(f"Livro coletado com sucesso: {dados['Title']}")
            except Exception as e:
                logging.error(f"Erro ao coletar dados do livro: {url} — {e}")

            driver.back()
            time.sleep(0.3)

        try:
            driver.find_element(By.CSS_SELECTOR, "li.next a").click()
            time.sleep(1)
        except Exception:
            print("Fim das páginas.")
            logging.info("Fim das páginas. Raspagem concluída.")
            break

    logging.info(f"Total de livros raspados: {livro_count}")
    return pd.DataFrame(livros)
