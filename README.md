# Ranking Socioeconômico dos Distritos de São Paulo com PCA

![Mapa Exemplo](/assets/image.png)  
*Visualização do ranking.*

## Visão Geral

Este projeto utiliza **Análise de Componentes Principais (PCA)** para reduzir a dimensionalidade de dados socioeconômicos dos distritos de São Paulo, criando um ranking baseado em fatores principais. Os resultados são visualizados em mapas estáticos e dinâmicos, oferecendo uma análise espacial clara e interativa. O objetivo é demonstrar habilidades em Machine Learning, manipulação de dados e visualização geoespacial, com foco em aplicações práticas para análise urbana.

- **Autor:** Wellington M Santos
- **Data:** Março 2025

## Objetivos

1. Reduzir variáveis socioeconômicas correlacionadas em componentes principais usando PCA.
2. Validar a adequação dos dados com testes estatísticos (KMO e Bartlett).
3. Gerar um ranking ponderado dos distritos com base nos fatores extraídos.
4. Visualizar os resultados em mapas interativos para insights espaciais.

## Tecnologias Utilizadas

- **Python 3.x**
- **Bibliotecas:**
  - `pandas` e `numpy`: Manipulação e análise de dados.
  - `scikit-learn`: Implementação do PCA e padronização.
  - `factor_analyzer`: Testes de adequação (KMO e Bartlett).
  - `geopandas`: Manipulação de dados geoespaciais.
  - `folium` e `mapclassify`: Visualização de mapas dinâmicos.
  - `plotly` e `matplotlib`: Gráficos interativos e estáticos.

## Estrutura do Projeto

- **`assets`**: Diretório com arquivos estáticos.
- **`data`**: Diretório com dataset e Shapefile contendo os limites geográficos dos distritos (fonte: [GeoSampa](http://geosampa.prefeitura.sp.gov.br/)).
- **`notebooks`**: Diretório com Notebook principal com o código comentado e visualizações.
- **`ranking_distritos.html`**: Arquivo gerado com o mapa interativo.

### Fluxo do Código

1. **Exploração Inicial:** Carregamento e inspeção dos dados.
2. **Preparação:** Cálculo da matriz de correlação e validação com KMO e Bartlett.
3. **PCA:** Padronização dos dados, extração de fatores e análise da variância explicada.
4. **Ranking:** Criação de um ranking ponderado com base nos dois primeiros fatores.
5. **Visualização:** Geração de mapas estáticos (`matplotlib`) e dinâmicos (`folium`).

## Resultados

- **Redução de Dimensionalidade:** Dois fatores principais (F1 e F2) foram selecionados pelo Critério de Kaiser, explicando ~68% da variância total.
- **Ranking:** Distritos foram ordenados com base em scores fatoriais ponderados.
- **Visualização:** Mapas destacam a distribuição espacial do ranking, com interatividade no formato HTML.

Exemplo de saída:  
- **Mapa Estático:** Mostra gradientes de cor para o ranking.  
- **Mapa Dinâmico:** Permite zoom e exploração com camadas adicionais (ex.: OpenStreetMap).

## Como Executar

### Pré-requisitos
- Python 3.8+ instalado.
- Ambiente virtual recomendado (ex.: `venv` ou `conda`).

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/esscova/ranking-socioeconomico-sp.git
   cd ranking-socioeconomico-sp
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Execução
1. Abra o notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```
2. Execute os blocos de código sequencialmente.
3. O mapa interativo será salvo como `ranking_distritos.html`.

## Destaques Técnicos

- **Validação Estatística:** Uso de testes KMO e Bartlett para garantir a adequação do PCA.
- **Visualização Avançada:** Integração de mapas dinâmicos com `folium`, ideal para análises interativas.
- **Código Modular:** Estrutura clara e comentada, fácil de adaptar para outros datasets.

## Contato

- **E-mail:** wsantos08@hotmail.com
- **LinkedIn:** https://www.linkedin.com/in/wellington-moreira-santos/
- **Portfólio:** [Link do portfólio]

