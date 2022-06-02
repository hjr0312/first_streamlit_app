import streamlit
streamlit.title('i love nubby')
streamlit.header('things i love about nubby:')
streamlit.text('hugs')
streamlit.text('kisses')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
