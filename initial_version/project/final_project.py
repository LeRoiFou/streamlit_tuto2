import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
from PIL import Image
import numpy as np
import plotly.express as px

def read_data():
    '''
    Conversion du fichier csv en dataframe pandas
        :return: chargement du fichier csv au format dataframe pandas
    '''
    return pd.read_csv('initial_version/project/s&p500.csv')

def parameter(df, sector_default_val, cap_default_val):
    """
    Alimentation des valeurs des widgets dont les valeurs du dataframe
        :param df: dataframe
        :param sector_default_val: valeur par défaut pour le secteur
        :return: option_sector, cap_value, dividend_value, profit_value
    """
    
    ##### SECTOR #####
    
    # Récupération des valeurs uniques de la colonne 'Sector' du dataframe
    sector_values = [sector_default_val] + list(df['sector'].unique())
    option_sector = st.sidebar.selectbox('Sector', sector_values, index=0)
    
    ##### MARKET CAP #####
    
    # Liste des valeurs pour la capitalisation
    cap_value_list = [cap_default_val] + ['Small', 'Medium', 'Large']
    cap_value = st.sidebar.selectbox('Capitalization', cap_value_list, index=0)
    
    ##### DIVIDEND #####
    dividend_value = st.sidebar.slider('Dividend rate between than (%)', 
                                       0.0, # valeur minimum
                                       10.0, # valeur maximum
                                       [0.0, 10.0], # valeurs modifiables
                                       )
    
    ##### PROFIT #####
    min_profit_value, max_profit_value = float(df['profitMargins_%'].min()
                                               ), float(df['profitMargins_%'].max())
    profit_value = st.sidebar.slider('Profit margin rate greater than (%)',
                                     min_profit_value, # valeur minimum
                                     max_profit_value, # valeur maximum
                                     step=10.0, # pas de 10
                                     )
    
    return option_sector, cap_value, dividend_value, profit_value

def filtering(df, sector_default_value, cap_default_value, option_sector, 
              cap_value, dividend_value, profit_value):
    """
    Filtrage du dataframe
        :param df: dataframe
        :param sector_default_value: valeur par défaut pour le secteur
        :param cap_default_value: valeur par défaut pour la capitalisation
        :param option_sector: secteur choisi
        :param cap_value: capitalisation choisie
        :param dividend_value: valeur du dividende
        :param profit_value: valeur du profit
        :return: dataframe filtré
    """
    
    #### Sector filtering ####
    if option_sector != sector_default_value:
        df = df[df['sector'] == option_sector]
        
    #### Market cap filtering ####
    if cap_value != cap_default_value:
        if cap_value == 'Small':
            df = df[df['marketCap'] <= 20e9]
        elif cap_value == 'Medium':
            df = df[(df['marketCap'] > 20e9) & (df['marketCap'] <= 100e9)]
        elif cap_value == 'Large':
            df = df[df['marketCap'] > 100e9]
            
    #### Dividend filtering ####
    df = df[
        (df['dividendYield_%'] >= dividend_value[0])
        & (df['dividendYield_%'] <= dividend_value[1])
        ]
    
    #### Profit filtering ####
    df = df[df['profitMargins_%'] >= profit_value]
    
    return df

def company_price(df, option_company):
    """
    
        :param df: dataframe chargée
        :param option_company: entreprise sélectionnée
    """
    # Si l'entreprise a été selectionnée
    if option_company != None:
        
        # Filtre de la DF : récupération de la valeur du champ 'name' à
        # partir de l'entreprise sélectionnée
        ticker_company = df.loc[df['name'] == option_company, 'ticker'].values[0]
        
        data_price = pdr.get_data_yahoo(ticker_company, 
                                        start="2011-12-31", 
                                        end="2021-12-31")['Adj Close']
        data_price = data_price.reset_index(drop = False)
        data_price.columns = ['ds','y']
        return data_price
    
    return None
        

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
    
    # Fonction permettant de retourner les quatres valeurs des widgets ajoutés
    sector_default_value = 'All'
    cap_default_value = 'All'
    option_sector, cap_value, dividend_value, profit_value = parameter(
        df, sector_default_value, cap_default_value)
    
    # Filtrage du dataframe
    df = filtering(df, sector_default_value, cap_default_value, option_sector, 
              cap_value, dividend_value, profit_value)
    
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

    # Part 2 - Choose a Company
    st.subheader('Part 2 - Choose a Company')
    option_company = st.selectbox('Choose a company:', df['name'].unique())
    
    # Part 3 - Stock analysis
    st.subheader("Part 3 - {} stock analysis".format(option_company))
    data_price = company_price(df, option_company)
    st.dataframe(data_price)
