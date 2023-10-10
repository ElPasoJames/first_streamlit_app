import streamlit
import pandas
import requests
import snowflake.connector

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
fruits_to_show = my_fruit_list.loc[fruits_selected]

#enables customer to pick a friot they want to add from dropdown
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#creates the actual table from fruit data
#streamlit.dataframe(my_fruit_list)
#chaged my_fruit_list to fruits_to_show
streamlit.dataframe(fruits_to_show)

#display fruityvice response
streamlit.header("Fruityvice Fruit Advice!")

#create text block for user to enter fruit choice
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
                
# Diisplay fruityvice API responce
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
######streamlit.text(fruityvice_response.json())
# enable pandas to fruityvice
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

#query data for snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
