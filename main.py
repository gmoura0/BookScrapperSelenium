import streamlit as st
import io
from pandas import DataFrame
from scraper import criar_driver, raspar_livros


def converter_csv(df: DataFrame) -> bytes:
    """
    Converte um DataFrame pandas em bytes CSV para download no Streamlit.

    Args:
        df (DataFrame): DataFrame a ser convertido.

    Returns:
        bytes: Conteúdo CSV codificado em UTF-8 com BOM.
    """
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, encoding="utf-8-sig", sep=";")
    return buffer.getvalue().encode("utf-8-sig")


def main() -> None:
    """
    Função principal da aplicação Streamlit que gerencia a interface,
    execução da raspagem e exibição dos resultados.
    """
    st.set_page_config(page_title="📘 Books Scraper", layout="wide")
    st.title("📘 Books — Raspagem com Selenium")

    if st.button("🚀 Iniciar raspagem"):
        with st.spinner("Raspando livros, aguarde..."):
            driver = criar_driver()
            df = raspar_livros(driver)
            driver.quit()
            st.session_state.df = df
        st.success(f"📚 {len(df)} livros coletados!")

    if "df" in st.session_state:
        df: DataFrame = st.session_state.df
        filtro: str = st.text_input("🔎 Filtrar por título")
        if filtro:
            df = df[df["Title"].str.contains(filtro, case=False, na=False)]

        st.dataframe(df, use_container_width=True)
        csv = converter_csv(df)
        st.download_button("📥 Baixar CSV", csv, "livros.csv", "text/csv")


if __name__ == "__main__":
    main()