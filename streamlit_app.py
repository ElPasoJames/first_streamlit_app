import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice
        streamlit.error("Please select a fruit to get information")
    else:
        # Diisplay fruityvice API responce
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        ######streamlit.text(fruityvice_response.json())
        # enable pandas to fruityvice
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()
                
#query data for snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.multiselect("What fruits would you like to add?:", list (my_fruit_list.index))
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.write('Thanks for adding', fruit_selected)

#add_my_fruit = streamlit.multiselect("What fruits would you like to add?:", list (my_fruit_list.index))
#fruits_to_show = my_fruit_list.loc[fruits_selected]

# Convert the list of fruits to a string
#fruits_selected_string = ', '.join(fruits_selected)

# Write the message to the Streamlit app
#streamlit.write('Thanks for adding', fruits_selected_string)

#add_my_fruit = streamlit.multiselect("What fruits would you like to add?:", list (my_fruit_list.index))
#fruits_selected_string = ', '.join(add_my_fruit)
# Move this line to the end of the code block
#streamlit.write('Thanks for adding', add_my_fruit)

#create fruit selection area for adding addition friut
add_my_fruit = streamlit.multiselect("What fruits would you like to add?:", list (my_fruit_list.index))
fruits_selected_string = ', '.join(add_my_fruit)
# Move this line to the end of the code block
streamlit.write('Thanks for adding {}'.format(fruits_selected_string))

#this code wont work and will throw a control flow error
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#dont run anything past here
streamlit.stop()
