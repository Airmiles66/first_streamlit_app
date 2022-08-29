import streamlit

streamlit.title('My first streamlit app is here')

streamlit.header('Breakfast favourites')
streamlit.text('\N{pot of food} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{broccoli} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{egg} Hard-Boiled Free-Range Egg')

streamlit.text('\N{banana} \N{strawberry} Build your own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


