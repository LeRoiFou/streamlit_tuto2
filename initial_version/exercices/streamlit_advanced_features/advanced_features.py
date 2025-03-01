"""
st.form permet d'interagir des widgets avec un bouton d'exécution, qui sont 
dans un formulaire : si on change un paramètre d'un wigdet dans un formulaire, 
streamlit ne va pas réexécuter à nouveau l'application

st.session_state permet de ne pas réinitialiser la valeur d'une valeur lorsqu'on
réexécute l'application

"""

import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr

def form():
    """
    Formulaire
    """
    # Sous-titre
    st.header("Streamlit form tutorial")
    
    # Formulaire contenant les widgets ci-après
    form = st.form(key='my-form')
    name = form.text_input('Enter your firstname')
    agree = form.checkbox('I agree')
    color = form.select_slider(
        'Select a color', options=['red', 'orange', 'yellow'])
    submit = form.form_submit_button('Submit')
    
    # Si le bouton est validé...
    if submit:
        st.write(f'Your name is {name}')
        st.write(f'Are you agree? {agree}')
        st.write(f'Your color is {color}')
        
def session():
    """
    Session
    """
    
    # Sous-titre
    st.header("Streamlit session tutorial")
    
    # Si la variable n'est pas en session
    if 'counter' not in st.session_state:
        # Création d'une variable en session
        st.session_state['counter'] = 0
        
    # Création d'une variable classique (qui n'est pas en session)
    not_a_session_state = 0
    
    # Bouton d'exécution
    if st.button('Click on me'):
        # Incrémentation des deux variables ci-avant
        st.session_state['counter'] += 1
        not_a_session_state += 1
        
    st.write(st.session_state.counter, "This is a session state value")
    st.write(not_a_session_state, "This is not a session state value")

if __name__ == '__main__':
    
    # Configuration de la page web
    st.set_page_config(
        page_title='Streamlit advanced features',
        page_icon='😎',
        layout='centered',
    )
    
    # Titre principal
    st.title('Streamlit adanced features')

    # Appel des fonctions ci-avant
    form()
    session()
    