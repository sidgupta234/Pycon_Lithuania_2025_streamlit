##### Libraries #####
import streamlit as st
import pandas as pd
import numpy as np
##### Libraries #####

##### Page config #####
# Wide Layout uses entire screen (I prefer),
# Centered restricts to centre 
st.set_page_config(page_title='Comic Fetcher', 
page_icon = "favicon.png", 
layout = 'wide', #wide / centered 
initial_sidebar_state = 'auto') #prefer auto

# # ##### Page config #####

#### Columns #####
# c1, c2, c3= st.columns((1, 2, 1))

# with c1:
#     st.write("hello")

# with c2:
#     st.write("Austria")
    
# with c3:
#     st.write("World")

# # ##### Columns #####

# # ##### Container #####

# c1, c2= st.columns((1, 2))

# header = st.container()

# with header and c1:
#     st.title("XKCD COMIC FETCHER")
#     st.header("Get 1 random Comic")

# # ##### Container #####

# # ##### Text Display Types #####

# c1, c2 = st.columns((1, 2))

# with c1:
#     st.markdown("<i>Markdown: We are having fun in Pycon Austria </i>", unsafe_allow_html=True)
#     st.title("Title: We are having fun in Pycon Austria")
#     st.header("Header: We are having fun in Pycon Austria")
#     st.subheader("Subheader: We are having fun in Pycon Austria")
#     st.caption("Caption: We are having fun in Pycon Austria")
#     st.code("Code: print(We are having fun in Pycon Austria)")
#     st.text("Text: We are having fun in Pycon Austria")
#     st.latex(r"\text{We}^{\text{are}} + \text{having}^{\text{fun}} = \text{Pycon}^{\text{Austria}}")

# # ##### Text Display Types #####

# # ##### Input Widgets #####

# c1, c2 = st.columns((1, 2))

# with c1:
#     if st.button('press'):
#         st.write('Button pressed')
#     else:
#         st.write('Button never pressed')
    
#     text_input = st.text_input("Enter your name")
#     st.write("Your name is ...", text_input)

#     # Select box example
#     option = st.selectbox(
#         'Choose your favorite comic genre:',
#         ('Sci-Fi', 'Fantasy', 'Humor', 'History', 'Romance')
#     )
#     st.write('You selected:', option)


# # ##### Input Widgets #####

# # ##### Charts #####

# # # c1, c2 = st.columns((1, 2))

# # # with c1:

# # #     chart_data = pd.DataFrame(
# # #         np.random.randn(20, 1),
# # #         columns=["a"])

# # #     st.bar_chart(chart_data)

# # ##### Charts #####

# # ##### Media #####

# # c1, c2 = st.columns((1, 2))

# # with c1:
# #     st.image("https://i.imgur.com/naDZBfE.jpeg")
    
# # ##### Media #####