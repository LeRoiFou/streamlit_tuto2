import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

def plotly():
    """
    Récupération d'un DF pour afficher les données dans des graphiques plotly
    """
    
    # Sous-titre
    st.header("Display graph with plotly")
    
    # Récupération des données dans une dataframe (pourboires <-> addition)
    df = px.data.tips()
    
    # Configuration des données en histogramme
    fig = px.histogram(df, 
                 x='total_bill', 
                 y='tip', 
                 color='sex',
                 marginal='box', # boîte à moustache
                 )
    
    # Affichage du graphique
    st.plotly_chart(fig)
    
def altair():
    """
    Récupération d'un DF pour afficher les données dans des graphiques altair
    """
    
    # Sous-titre
    st.header("Display graph with altair")
    
    # Configuration de la DF
    df = pd.DataFrame(
        np.random.rand(200, 3),
        columns=['a', 'b', 'c']
    )
    
    # Configuration du graphique
    fig = alt.Chart(df).mark_circle().encode(
        x='a',
        y='b',
        size='c',
        color='c',
        tooltip=['a', 'b', 'c'],
    )
    
    # Affichage du graphique
    st.altair_chart(fig, use_container_width=True)
    
def map():
    """
    Affichage des coordonnées et des GPS d'une carte
    """
    
    # Sous-titre
    st.header("Display a map with Open Street Map")
    
    # Configuration de la DF
    df = pd.DataFrame(
        np.random.rand(200, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon',]
    )
    
    # Affichage de la carte
    st.map(df)
    

if __name__ == '__main__':
    
    # Configuration de la fenêtre
    st.set_page_config(
        page_title="Streamlit visualisation app",
        layout='centered',
    )
    
    #Titre principal
    st.title('Visualization tutorial for streamlit')
    
    # Fonctions définies ci-avant
    plotly()
    altair()
    map()
