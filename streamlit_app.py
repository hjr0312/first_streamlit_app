import streamlit
streamlit.title('i love nubby')
streamlit.header('things i love about nubby:')
streamlit.text('hugs')
streamlit.text('kisses')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick favorite",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('fruityvice fruit advice!')
fruit_choice = streamlit.text_input('what fruit would you like information about?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
