import streamlit as st
import pandas as pd
from PIL import Image

def read_data():
    '''
    return : chargement du fichier csv au format dataframe pandas
    '''
    return pd.read_csv('initial_version/project/s&p500.csv')

if __name__ == '__main__':
    
    # Configuration de la fenêtre
    st.set_page_config(
        page_title='Udemy project', 
        page_icon="📈", 
        initial_sidebar_state='expanded',
        )
    
    # Titre principal
    st.title('S&P500 Screaner & Analysis')
    
    # Barre latérale
    st.sidebar.title('Search criteria')
    
    # Image à charger
    image = Image.open('initial_version/project/stock.jpeg')
    
    # Intervention uniquement sur la col 2 avec [1, 3, 1] = taille des colonnes
    _, col_image2, _ =st.columns([1, 3, 1])
    with col_image2:
        st.image(image, caption='@austindistel',)
    
    # Appel de la méthode read_data()
    df = read_data()
    
    # Sous-titre
    st.subheader('Part 1 - S&P500 Screener')
    
    # Expension de la partie 1
    with st.expander('Part 1 - explanation', expanded=False):
        st.write("""
            In the table below, you will find most of the companies in the S&P500 (stock market index of the 500 largest American companies) with certain criteria such as :
                
                - The name of the company
                - The sector of activity
                - Market capitalization
                - Dividend payout percentage (dividend/stock price)
                - The company's profit margin in percentage
            
            ⚠️ This data is scrapped in real time from the yahoo finance API. ⚠️

            ℹ️ You can filter / search for a company with the filters on the left. ℹ️
        """)
        
        # Nombre de lignes dans le dataframe
        st.write("Number of companies :", df.shape[0])
        
        # Affichage du dataframe excluant la première colonne
        st.dataframe(df.iloc[:, 1:])
