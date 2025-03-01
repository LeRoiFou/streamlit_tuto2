import streamlit as st
import pandas as pd
import numpy as np
import datetime

def button():
    
    st.header("Button")
    
    # Création d'un bouton
    button = st.button("Click me")
    st.write(f'Click status : {button}')
    
def checkbox():
    
    st.header("Checkbox")

    # Création d'une checkbox
    checkbox = st.checkbox("I agree")
    st.write(f'Check status : {checkbox}')
    
def diff_button_checkbox():
    
    st.header('Difference between button and checkbox')
    
    st.write(" The value of a button is re-initialized at each new run of the application. And as by default a streamlit application is restarted after each interaction with the user, this will force the value of a button to return to its default value (False). While for a checkbox, the value is kept between 2 successive runs of the application. The use of a checkbox or a button depends on the use you want to make. ")

def radio_button():
    
    st.header("Radio Button")
    
    # Création d'un radio button
    color = st.radio("Choose your favorite color: ", 
                     ["Green", "Blue", "Red"],
                     index=1, # valeur par défaut
                     )
    st.write(f'You chose {color}')

def select_box():
    
    st.header("Select Box")
    
    # Création d'une select box
    color = st.selectbox("What's your favorite color? ", 
                         ["Green", "Blue", "Red"],
                          index=1, # valeur par défaut
                          )
    st.write(f'You chose {color}')
    
def multi_select():
    
    st.header("Multi Select")
    
    # Création d'une multi select box
    colors = st.multiselect("What's your favorite color? ", 
                            ["Green", "Blue", "Red"],
                            default=["Green", "Blue"],
                            )
    st.write(f'You chose {colors}')
    
def slider():
    
    st.header("Slider")
    
    # Création d'un slider
    number = st.slider("Insert a number ", 
                    min_value=5, 
                    max_value=15, 
                    value=10, # valeur par défaut
                    )
    st.write(f'The number is: {number}')
    
def number_input():
    st.header("Number Input")
    
    st.number_input("Insert a number ",
                    min_value=5,
                    max_value=15,
                    value=10, # valeur par défaut
                    )
    
def date_input():
    st.header("Date")
    
    date_value = st.date_input("When is your birthday date? ",
                  min_value=datetime.date(1925, 1, 1),
                  max_value=datetime.date(2024, 12, 31),
                  value=datetime.date(1977, 6, 1), # valeur par défaut
                  )
    st.write(f"The birthdate is: {date_value}")
    
def camera_input():
    st.header("Camera")
    
    picture = st.camera_input("Take a picture")
    if picture:
        st.image(picture, caption="Your picture",)


if __name__ == '__main__':
    # Configuration de la page web
    st.set_page_config(
        page_title="Streamlit Interactions App",
        layout='centered',
        page_icon="🧊",
        )
    
    # Titre de la page
    st.title("Wigdets tutorial for streamlit")

    # Appel des fonctions pour les différents widgets
    # button()
    # checkbox()
    # diff_button_checkbox()
    # radio_button()
    # select_box()
    # multi_select()
    slider()
    number_input()
    date_input()
    camera_input()
