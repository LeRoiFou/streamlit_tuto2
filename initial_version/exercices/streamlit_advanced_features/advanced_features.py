"""
st.form permet d'interagir des widgets avec un bouton d'exécution, qui sont 
dans un formulaire : si on change un paramètre d'un wigdet dans un formulaire, 
streamlit ne va pas réexécuter à nouveau l'application
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

if __name__ == '__main__':
    
    # Configuration de la page web
    st.set_page_config(
        page_title='Streamlit advanced features',
        layout='centered',
    )
    
    # Titre principal
    st.title('Streamlit adanced features')

    # Appel des fonctions ci-avant
    form()
