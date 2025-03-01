import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import folium_static

# Configurações iniciais
st.set_page_config(
    layout="wide",
    page_title="Ranking Socioeconômico dos Distritos de São Paulo",
    page_icon="🌃"
)

# Carregamento dos dados
dados_completos = gpd.read_file('./data/dados_completos.geojson')

# Sidebar - Links e Contatos
st.sidebar.info("Sobre")
st.sidebar.text("Simplificando dados socioeconômicos com PCA para um ranking significativo.")
st.sidebar.markdown("""
- **Repositório:** [GitHub](https://github.com/esscova/ranking-socioeconomico-sp)  
- **Autor:** Wellington M Santos  
- **E-mail:** wsantos08@hotmail.com  
- **LinkedIn:** [in/wellington-moreira-santos](https://www.linkedin.com/in/wellington-moreira-santos/)
""")
st.sidebar.markdown("\n")

# Sidebar - Configurações com Expander
with st.sidebar.expander("⚙️ Configurações", expanded=True):
    st.subheader("Filtro de Distritos")
    distritos_opcoes = ["Todos"] + dados_completos['distritos'].tolist()
    selecao_distritos = st.multiselect(
        "Selecione os distritos para visualizar:",
        options=distritos_opcoes,
        default=["Todos"],  # "Todos" como padrão
        help="Escolha distritos ou 'Todos' para ver tudo.",
        key="distritos_select"
    )

    # Lógica de filtragem
    if "Todos" in selecao_distritos or not selecao_distritos:
        dados_filtrados = dados_completos
    else:
        dados_filtrados = dados_completos[dados_completos['distritos'].isin(selecao_distritos)]


# download
st.sidebar.markdown("\n")
st.sidebar.subheader("Exportar Dados")
csv = dados_filtrados[['distritos', 'Ranking']].to_csv(index=False)
st.sidebar.download_button(
    label="Baixar Ranking como CSV",
    data=csv,
    file_name="ranking_distritos_sp.csv",
    mime="text/csv",
    key="download_btn"
)

# Título principal
st.title("Ranking Socioeconômico dos Distritos de São Paulo")

# Informações sobre o projeto e PCA
with st.expander("ℹ️ Sobre o Projeto e PCA", expanded=False):
    st.markdown("""
    ### Sobre o Projeto
    Este projeto utiliza **Análise de Componentes Principais (PCA)** para reduzir a dimensionalidade de dados socioeconômicos dos distritos de São Paulo, gerando um ranking baseado em dois fatores principais. Os resultados são visualizados em um mapa interativo, oferecendo insights espaciais sobre a distribuição socioeconômica na cidade.

    - **Objetivo:** Simplificar variáveis correlacionadas (ex.: renda, educação) e criar um ranking significativo.
    - **Dados:** Dataset `distritos_sp.csv` e shapefile do GeoSampa.
    - **Tecnologias:** Python, Pandas, Scikit-learn, Geopandas, Folium, Streamlit.

    ### Detalhes Técnicos do PCA
    - **Pré-processamento:** Dados padronizados com Z-Score para igualar escalas.
    - **Validação:** Testes KMO (>0.6) e Bartlett (p<0.05) confirmaram a adequação.
    - **Fatores:** Dois componentes principais (F1 e F2) selecionados pelo Critério de Kaiser, explicando ~68% da variância.
    - **Ranking:** Calculado como soma ponderada dos scores fatoriais (F1 e F2) pela variância explicada.
    """)

# Layout com colunas
col1, col2 = st.columns([1, 3])

# Coluna 1 - Tabela de Ranking
with col1:
    st.subheader("Top 10 Distritos")
    styled_df = (dados_filtrados[['distritos', 'Ranking']]
                 .sort_values('Ranking', ascending=False)
                 .head(10)
                 .style.format({'Ranking': '{:.2f}'})
                 )
    st.dataframe(styled_df, height=400)

# Coluna 2 - Mapa Interativo
with col2:
    st.subheader("Mapa Interativo")
    mapa = dados_filtrados.explore(
        column='Ranking',
        cmap='seismic_r',
        tooltip='distritos',
        tooltip_kwds={'labels': False},
        name='Distritos SP',
        height=600,
        width=1000
    )
    folium.TileLayer('OpenStreetMap').add_to(mapa)
    folium.LayerControl().add_to(mapa)
    folium_static(mapa, width=1000, height=600)