import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import data from s3 DB to create a table
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# change the table index to use fruit names rather than table number
my_fruit_list = my_fruit_list.set_index('Fruit')

#gives a few starter suggestions in the drop down selector
#streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado','Strawberries'])
#added fruits selected the the code
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado','Strawberries'])

#enables customer to pick a friot they want to add from dropdown
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#creates the actual table from fruit data
#streamlit.dataframe(my_fruit_list)
#chaged my_fruit_list to fruits_to_show
streamlit.dataframe(fruits_to_show)
