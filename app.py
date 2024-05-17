import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
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

    st.write("## Feedback")
    st.write("""
    Se você tiver alguma sugestão, feedback ou encontrar algum problema com o aplicativo, por favor, sinta-se à vontade para entrar em contato conosco.
    Sua opinião é muito importante para nós!
    """)


def grafico_linhas():
    st.title("grafico de linhas")
    data = pd.read_csv("Pokemon.csv")
    fig = plt.figure(figsize=(10,10)) 
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
    data = pd.read_csv("Pokemon.csv")
    st.title("grafico de barras")
    fig=plt.figure(figsize=(10,8))
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
    data = pd.read_csv("Pokemon.csv")
    st.title("grafico boxplot")
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
    st.title("Grafico de pizza")
    dados= pd.read_csv("Pokemon.csv")   
    legendary_counts = dados['legendary'].value_counts()
    fig=plt.figure(figsize=(10,13))
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
    selection = st.sidebar.selectbox("Ir para", list(pages.keys()))
    
    st.sidebar.title("Sobre")
    st.sidebar.write("projeto com o intuito de demonstrar algumas funcionalidades básicas da biblioteca matplotlib")
    # Executar a função correspondente à página selecionada
    pages[selection]()

if __name__ == "__main__":
    main()