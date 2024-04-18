import streamlit as st 
from streamlit_option_menu import option_menu

import app
from pdf_chat_bot import app1

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            application = option_menu(
                menu_title='Operations',
                options=['Audio & Image','Pdf Summarizer'],
                icons=['house-fill','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if application == "Audio & Image":
            app.main()
        if application == "Pdf Summarizer":
            app.ForPDFmain()   
            
    run()      