"""
Documentation : https://docs.streamlit.io/
"""

import streamlit as st
import pandas as pd
from PIL import Image

def connect_data_csv():
    
    # Titre
    st.header("Streamlit connect data tutorial") 
    
    MY_PATH = 'C:/Users/LRCOM/Documents/Professionnel/Python/streamlit_udemy/initial_version/project/s&p500.csv'
    
    # Chargement et affichage des données
    data = pd.read_csv(MY_PATH)
    st.dataframe(data)
    
    # Méthode style : met en évidence la valeur maximale de chaque colonne
    st.dataframe(data.style.highlight_max(axis=0)) 
    
def display_write():
    
    st.header("Streamlit display text tutorial")
    
    # Hierarchie des textes
    st.title('title')
    st.header('hearder')
    st.subheader('subheader')
    st.write('write')
    st.text('text')
    st.caption('caption')
    
    # Affichage d'un code python
    code='''
    def hello():
        print('hello')
    '''
    st.code(code, language='python')
    
    # Markdown HTML
    st.markdown(f'<h1 style="color: #ff5733; font-size:24px;">HTML text</h1>', 
                unsafe_allow_html=True # True : permet d'afficher du HTML
                )
    
def display_media():
        
    st.header("Streamlit display media tutorial")
    
    # Affichage d'une image
    image = Image.open('initial_version/exercices/streamlit_basics/stock.jpeg')
    st.image(image, 
             caption='@austindistel', # Crédit de l'image
             width=250)
    
def display_audio():
    
    st.subheader('Audio')
    
    # Chargement d'un fichier audio
    audio_file = open('initial_version/exercices/streamlit_basics/audio.ogg', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    
def display_video():
    
    st.subheader('Video')
    
    # Chargement d'un fichier vidéo
    video_file = open('initial_version/exercices/streamlit_basics/video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4')
    
def layout():
    
    st.subheader('Streamlit layout tutorial')
    
    # Création d'un menu vertical
    st.sidebar.title('Sidebar title')
    st.sidebar.write('Sidebar text')
    st.sidebar.metric(label="Température", value="25°C", delta="1°C")
    
    # Colonnes
    col1, col2 = st.columns(2)
    with col1:
        st.header('First column')
        st.write('Hello 1')
    with col2:
        st.header('Second column')
        st.write('Hello 2')
        
    # Containers
    with st.container():
        st.header('First Container')
        st.write('Hello container 1')
    with st.container():
        st.header('Second Container')
        st.write('Hello container 2')
        
    # Extenseurs
    st.header('Expander')
    with st.expander('This is an expander'):
        st.write("""
                 Streamlit tutorial for expander
                 """)
    
    
if __name__ == '__main__':
    
    # Configuration de la page web
    st.set_page_config(
        page_title="Streamlit Basics app", # Titre de la fenêtre
        layout="centered", # Centrer le contenu
    )
    
    # Titre principal
    st.title("Streamlit fundamentals tutorial")

    # connect_data_csv()
    
    # display_write()
    
    display_media()
    
    display_audio()
    
    display_video()
    
    layout()
