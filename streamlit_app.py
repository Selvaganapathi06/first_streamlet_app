import streamlit
streamlit.title('Hello Selva')
streamlit.header('Hello')
streamlit.text('Hello World')
streamlit.text('How are you?')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


streamlit.dataframe(my_fruit_list)
