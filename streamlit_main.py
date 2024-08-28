import base64
import streamlit as st
import pandas as pd
import numpy as np
import random
import set_backgroung_image


def main():
    st.set_page_config(layout="wide")

    #Setting the background image
    set_backgroung_image.set_backgroung_image()

    cocktails= pd.read_csv(r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\cocktail_recommendation\cocktails_final_data.csv");

    # Get unique alcohol types
    unique_alcohol_types = cocktails['alcohol_type'].explode().dropna().unique()
    alcohol_genre = cocktails['alcohol_genre'].unique()


    # Define the image paths
    img_path_vodka = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\coctail_vodka.png"
    img_path_beer = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\cocktail_beer.png"
    img_path_gin_tonic = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\gin-tonic.png"
    img_path_gin = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\gin.png"
    img_path_whiskey = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\whiskey.png"
    img_path_cocktail = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\cocktail.png"
    img_path_cocktail1 = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\cocktail_1.png"
    img_path_maithai = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\mai-thai.png"
    img_path_mojito = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\mojito.png"
    img_path_heading = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\heading.png"


    img_path_Amaretto_Sourball = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\Amaretto_Sourball.png"
    img_path_Southside_Fizz = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\Southside_Fizz.png"
    img_path_The_Mad_King = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\The_Mad_King.png"
    img_path_coffee_please = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\coffee_please.png"
    img_path_Peter_pumpkin = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\Peter_pumpkin.png"
    img_path_big_n_bright = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\big_n_bright.png"
    img_path_strike_no_3 = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\strike_no_3.png"
    img_path_a_bloody_shame = r"C:\Users\Vaishali\Desktop\Vaishu\ISB\Term 3\ML-USL2\Assignment\a_bloody_shame.png"




    # Read the image files
    img_vodka = open(img_path_vodka, "rb").read()
    img_beer = open(img_path_beer, "rb").read()
    img_gin = open(img_path_gin, "rb").read()
    img_gin_tonic = open(img_path_gin_tonic, "rb").read()
    img_whiskey = open(img_path_whiskey, "rb").read()
    img_cocktail = open(img_path_cocktail, "rb").read()
    img_cocktail_1 = open(img_path_cocktail1, "rb").read()
    img_maithai = open(img_path_maithai, "rb").read()
    img_mojito = open(img_path_mojito, "rb").read()
    img_heading = open(img_path_heading, "rb").read()

    img_Amaretto_Sourball = open(img_path_Amaretto_Sourball, "rb").read()
    img_Southside_Fizz = open(img_path_Southside_Fizz, "rb").read()
    img_The_Mad_King = open(img_path_The_Mad_King, "rb").read()
    img_coffee_please = open(img_path_coffee_please, "rb").read()
    img_Peter_pumpkin = open(img_path_Peter_pumpkin, "rb").read()
    img_big_n_bright = open(img_path_big_n_bright, "rb").read()
    img_strike_no_3 = open(img_path_strike_no_3, "rb").read()
    img_a_bloody_shame = open(img_path_a_bloody_shame, "rb").read()


    unique_alcohols = cocktails['alcohol_type'].explode().unique().tolist()



    ###Main screen

    custom_style = """
    <style>
    /* Replace 'CustomFont' with the desired font name or font-family */
    .custom-font {
        font-family: 'CustomFont', Covered By Your Grace;
        font-size: 20px;
        color: #Cfff88; /* Replace with the desired text color */
        text-align: center;
        /* Add more CSS styles here as needed */
    }
    </style>
    """
    # Display the custom CSS style using 'st.markdown'
    st.markdown(custom_style, unsafe_allow_html=True)

    # Use the custom CSS class to style the text in st.write
    st.write('<p class="custom-font">Welcome to the ultimate cocktail customization experience! Unleash your taste buds and create the perfect drink that perfectly matches your style and preferences. Explore an array of exciting options, and let our system recommend the most thrilling cocktails just for you!</p>', unsafe_allow_html=True)





    with st.container():
         col1, col2 , col3 = st.columns(3)
         with col1:
             st.image(img_heading, use_column_width=False, width=390)
             st.image(img_Amaretto_Sourball, use_column_width=False, width=260)
             st.image(img_Southside_Fizz, use_column_width=False, width=260)
             st.image(img_The_Mad_King, use_column_width=False, width=260)
             st.image(img_coffee_please, use_column_width=False, width=260)
             st.image(img_Peter_pumpkin, use_column_width=False, width=320)
             st.image(img_big_n_bright, use_column_width=False, width=400)
             st.image(img_strike_no_3, use_column_width=False, width=260)
             st.image(img_a_bloody_shame, use_column_width=False, width=260)



         with col3:
             with st.container():
                 col31, col32,col33,col34 = st.columns(4)
                 with col31:
                     st.image(img_cocktail, use_column_width=False, width=80)
                 with col32:
                     st.image(img_cocktail_1, use_column_width=False, width=80)
                 with col33:
                     st.image(img_maithai, use_column_width=False, width=80)
                 with col34:
                     st.image(img_mojito, use_column_width=False, width=80)

             st.divider()

             st.markdown("<h3 style='color: #Cfff88;'>R &nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp; THAT</h3>", unsafe_allow_html=True)


             if 'button_clicked' not in st.session_state:
                 st.session_state.button_clicked = False

             def click_button():
                st.session_state.button = not st.session_state.button

             # Check if the button is clicked
             if st.button("\nRaise Your Glass to Creativity! Choose Your Cocktail Base!!!\n"):
                 st.session_state.button_clicked = True



             if st.session_state.button_clicked:

                st.markdown("***Choose your base:***")
                default_alcohol_base = "Choose your alcohol base"
                alcohol_genre_options = [default_alcohol_base] + [str(base) for base in unique_alcohols]

                selected_base = st.selectbox(
                    "Choose your alcohol base",
                    alcohol_genre_options
                )

                selected_base = [selected_base] if isinstance(selected_base, str) else selected_base


                filtered_cocktails_1 = cocktails[
                    cocktails['alcohol_type'].isin(selected_base)
                    ]
                if not filtered_cocktails_1.empty:
                    random_row_index = random.choice(filtered_cocktails_1.index)
                    top_5_similar_cocktails_indices_str = filtered_cocktails_1.loc[random_row_index, 'top_5_similar_cocktails']

                    # Convert the string to a list of integers
                    top_5_similar_cocktails_indices = [int(idx) for idx in top_5_similar_cocktails_indices_str.strip('[]').split(', ')]

                    # Get the DataFrame with the rows corresponding to the indices
                    top_5_similar_cocktails_df = cocktails.loc[top_5_similar_cocktails_indices, :]

                    # Extract 'Cocktail Name' and 'Preparation' columns from the new DataFrame
                    cocktail_names = top_5_similar_cocktails_df['Cocktail Name'].tolist()
                    preparations = top_5_similar_cocktails_df['Preparation'].tolist()
                    st.markdown("<h4 style='color: #Cfff88;'>Here are the top 5 cocktails that will best fit your taste based on your chosen Cocktail base!!'</h4>", unsafe_allow_html=True)
                    for name in cocktail_names:
                        st.write(f"{name}")
                    with st.expander("Click here to discover how these delightful cocktails are prepared"):
                        for name, prep in zip(cocktail_names, preparations):
                            st.write(f"{name} - {prep}")




             else:
                 st.markdown("Click the button above to choose your Base.")


         with col2:
             with st.container():
                 col21, col22,col23,col24,col25 = st.columns(5)
                 with col21:
                     st.image(img_vodka, use_column_width=False, width=80)
                 with col22:
                     st.image(img_beer, use_column_width=False, width=80)
                 with col23:
                     st.image(img_gin, use_column_width=False, width=80)
                 with col24:
                     st.image(img_gin_tonic, use_column_width=False, width=80)
                 with col25:
                     st.image(img_whiskey, use_column_width=False, width=80)

             st.divider()
             st.markdown("<h3 style='color: #Cfff88;'>THIS &nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "&nbsp;&nbsp;&nbsp;&nbsp; O</h3>", unsafe_allow_html=True)

             # Initialize session state
             if 'button_clicked' not in st.session_state:
                 st.session_state.button_clicked = False

             # Check if the button is clicked
             if st.button("\nCraft Your Flavor Fantasy! Pick Your Cocktail Genre!!!\n"):
                 st.session_state.button_clicked = True



             if st.session_state.button_clicked:
                 st.markdown("***Choose your alcohol genre***")
                 default_alcohol_genre = "Choose your alcohol genre"
                 alcohol_genre_options = [default_alcohol_genre] + [str(genre) for genre in alcohol_genre]
                 selected_alcohol_genre = st.selectbox(
                     'Select the alcohol genre you enjoy',
                     alcohol_genre_options,
                     index=0
                 )

                 selected_alcohol_genre = [selected_alcohol_genre] if isinstance(selected_alcohol_genre, str) else selected_alcohol_genre
                 filtered_cocktails = cocktails[
                     cocktails['alcohol_genre'].isin(selected_alcohol_genre)]

                 # cocktail_genre = filtered_cocktails['cocktail_genre'].unique()
                 #
                 # default_cocktail_genre = "Select the cocktail genre you enjoy"
                 # cocktail_genre_options = [default_cocktail_genre] + [str(genre) for genre in cocktail_genre]
                 # selected_cocktail_genre  = st.selectbox(
                 #     'Select the cocktail genre you enjoy',
                 #     cocktail_genre_options,
                 #     index=0
                 # )

                 selected_alcohol_genre = [selected_alcohol_genre] if isinstance(selected_alcohol_genre, str) else selected_alcohol_genre



                 filtered_cocktails = cocktails[
                     cocktails['alcohol_genre'].isin(selected_alcohol_genre)

                     ]

                 if not filtered_cocktails.empty:
                     random_row_index = random.choice(filtered_cocktails.index)
                     top_5_similar_cocktails_indices_str = filtered_cocktails.loc[random_row_index, 'top_5_similar_cocktails']

                     # Convert the string to a list of integers
                     top_5_similar_cocktails_indices = [int(idx) for idx in top_5_similar_cocktails_indices_str.strip('[]').split(', ')]

                     # Get the DataFrame with the rows corresponding to the indices
                     top_5_similar_cocktails_df = cocktails.loc[top_5_similar_cocktails_indices, :]

                     # Extract 'Cocktail Name' and 'Preparation' columns from the new DataFrame
                     cocktail_names = top_5_similar_cocktails_df['Cocktail Name'].tolist()
                     preparations = top_5_similar_cocktails_df['Preparation'].tolist()
                     st.markdown("<h4 style='color: #Cfff88;'>Here are the top 5 cocktails that will best fit your taste based on your chosen Cocktail genre!!!</h4>", unsafe_allow_html=True)
                     for name in cocktail_names:
                         st.write(f"{name}")
                     with st.expander("Click here to discover how these delightful cocktails are prepared"):
                         for name, prep in zip(cocktail_names, preparations):
                             st.write(f"{name} - {prep}")



             else:
                # Display a placeholder message until the button is clicked
                st.markdown("Click the button above to choose your genre.")

if __name__ == "__main__":
    main()