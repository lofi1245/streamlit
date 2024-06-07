import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd

#função para carregar os dados do dataframe so uma vez 
def carregar_dados():
    data = pd.read_csv("Pokemon.csv")
    return data

# Página inicial
def home():
    st.title('Bem-vindo ao Projeto Pokemon Data Visualization')
    st.write("""
    Este aplicativo é uma demonstração das funcionalidades básicas da biblioteca Matplotlib para visualização de dados dos Pokemon.
    Use a barra lateral para navegar entre diferentes tipos de gráficos e explorar os dados disponíveis.
    """)

    st.write("## Instruções de Navegação")
    st.write("""
    Na barra lateral à esquerda, você encontrará opções para acessar diferentes tipos de gráficos:
    - **Linhas**: Visualize a tendência de HP dos Pokemon ao longo das gerações.
    - **Barras**: Veja a distribuição de Pokemon por tipo.
    - **Boxplot**: Explore a distribuição das estatísticas dos Pokemon.
    - **Pizza**: Descubra a proporção de Pokemon lendários.
    """)



    st.write("## Sobre o Projeto")
    st.write("""
    Este projeto foi desenvolvido com o intuito de demonstrar algumas funcionalidades básicas da biblioteca Matplotlib em visualização de dados.
    Os dados utilizados são provenientes do conjunto de dados de Pokemon disponível no Kaggle.
    """)



def grafico_linhas():
    st.title("Gráfico de linhas")
    data = carregar_dados()
    fig = plt.figure(figsize=(10,10)) 
    
    # Agrupa os dados pelo valor da coluna 'generation' e calcula a média dos valores da coluna 'hp' para cada grupo.
    # Em seguida, plota esses valores médios em um gráfico, usando um marcador 'o' para cada ponto.
    data.groupby('generation')['hp'].mean().plot(marker='o')
    plt.title('Tendência de HP dos Pokemon ao Longo das Gerações')
    plt.xlabel('Geração')
    plt.ylabel('Média de HP')
    plt.grid(True)
    st.pyplot(fig)
    
    #aba para mosrar o codigo gerador do grafico 
    with st.expander('Código para gerar o gráfico'):
        with st.echo():
            data = pd.read_csv("Pokemon.csv")
            fig = plt.figure(figsize=(10,10)) 
            data.groupby('generation')['hp'].mean().plot(marker='o')
            plt.title('Tendência de HP dos Pokemon ao Longo das Gerações')
            plt.xlabel('Geração')
            plt.ylabel('Média de HP')
            plt.grid(True)
            
            
def grafico_barras():
    data = carregar_dados()
    st.title("Gráfico de barras")
    fig=plt.figure(figsize=(10,8))
    
    # Concatena as colunas 'type1' e 'type2' da DataFrame 'data', e então conta a frequência de cada valor
    # nas duas colunas combinadas, resultando em uma série com a contagem de cada tipo
    type_counts = pd.concat([data['type1'], data['type2']]).value_counts()
    type_counts.plot(kind='bar')
    plt.title('Distribuição de Pokemon por Tipo')
    plt.xlabel('Tipo')
    plt.ylabel('Número de Pokemon')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    st.pyplot(fig)
    
    #aba para mosrar o codigo gerador do grafico 
    with st.expander('Código para gerar o gráfico'):
        #exibe o codigo como texto 
        with st.echo():
            data= pd.read_csv("Pokemon.csv")
            fig=plt.figure(figsize=(10,8))
            type_counts = pd.concat([data['type1'], data['type2']]).value_counts()
            type_counts.plot(kind='bar')
            plt.title('Distribuição de Pokemon por Tipo')
            plt.xlabel('Tipo')
            plt.ylabel('Número de Pokemon')
            plt.xticks(rotation=45)
            plt.grid(axis='y')  
            
def grafico_boxplot():
    data = carregar_dados()
    st.title("Gráfico boxplot")
    fig=plt.figure(figsize=(10,8))
    stats = data[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
    stats.boxplot()
    plt.title('Distribuição das Estatísticas dos Pokemon')
    plt.ylabel('Valores')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    st.pyplot(fig)
    
    #aba para mosrar o codigo gerador do grafico 
    with st.expander('Código para gerar o gráfico'):
        with st.echo():
            data= pd.read_csv("Pokemon.csv")
            fig=plt.figure(figsize=(10,8))
            stats = data[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
            stats.boxplot()
            plt.title('Distribuição das Estatísticas dos Pokemon')
            plt.ylabel('Valores')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            
def grafico_pizza():
    st.title("Gráfico de pizza")
    dados= carregar_dados()   
    legendary_counts = dados['legendary'].value_counts()
    fig=plt.figure(figsize=(10,10))
    
    # Cria um gráfico de pizza a partir dos dados em 'legendary_counts'.
    # Os rótulos das fatias são definidos como 'Não Lendário' e 'Lendário'.
    # 'autopct' é usado para mostrar a porcentagem de cada fatia no gráfico.
    # 'startangle' define o ângulo inicial do gráfico, aqui definido como 140 graus para melhor visualização.
    plt.pie(legendary_counts, labels=['Não Lendário', 'Lendário'], autopct='%1.1f%%', startangle=140)
    plt.title('Proporção de Pokemon Lendários')
    plt.axis('equal')
    
    st.pyplot(fig)

    
    #aba para mosrar o codigo gerador do grafico    
    with st.expander('Código para gerar o gráfico'):
        with st.echo():
            dados= pd.read_csv("Pokemon.csv")
            legendary_counts = dados['legendary'].value_counts()
            fig=plt.figure(figsize=(10,13))
            plt.pie(legendary_counts, labels=['Não Lendário', 'Lendário'], autopct='%1.1f%%', startangle=140)
            plt.title('Proporção de Pokemon Lendários')
            plt.axis('equal')
    
         
            

# Função principal para rotear páginas
def main():

    # Configurar barra lateral para navegação entre páginas
    st.sidebar.title('Navegação')
    pages = {
        "Página Inicial": home,
        "Linhas": grafico_linhas,
        "Barras": grafico_barras,
        "Boxplot": grafico_boxplot,
        "Pizza": grafico_pizza
    }
    
    # Adiciona uma caixa de seleção na barra lateral com as opções das páginas disponíveis
    # e armazena a seleção do usuário na variável 'selection'.
    selection = st.sidebar.selectbox("Ir para", list(pages.keys()))
    
    st.sidebar.title("Sobre")
    st.sidebar.write("projeto com o intuito de demonstrar algumas funcionalidades básicas da biblioteca matplotlib")
    # Executar a função correspondente à página selecionada
    pages[selection]()

if __name__ == "__main__":
    main()