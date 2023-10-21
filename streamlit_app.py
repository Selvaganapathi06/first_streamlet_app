import streamlit
streamlit.title('Hello Selva')
streamlit.header('Hello')
streamlit.text('Hello World')
streamlit.text('How are you?')

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
