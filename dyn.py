import streamlit as st
import os
from PIL import Image

# CSS style for the background, text color, and headings
background_color = "#cdc5ba"  # Dark brown/black color resembling coffee
text_color = "#FFFFFF"  # White text color for better visibility
heading_color = "#4CAF50"  # Green heading color for emphasis

html_code = f"""
<style>
    [data-testid="stAppViewContainer"] {{
        background-color: {background_color};
        color: {text_color};
        font-family: 'Times New Roman', Times, serif; 
        padding: 3rem; /* Adjust padding as needed */
    }}

    [data-testid="stHeader"] {{
        background-color: #5c1500;
        color: {text_color};
        font-family: 'Times New Roman', Times, serif; 
        padding: 0px;
    }}

    h1, h2, h3 {{
        color: {heading_color};
    }}
    input[type="text"],
    input[type="email"],
    textarea,
    button[type="submit"] {{
        margin-bottom: 1rem; /* Add spacing between elements */
        padding: 0.5rem; /* Adjust padding */
        width: 100%; /* Make elements full width */
    }}
    button[type="submit"] {{
        background-color: #4CAF50; /* Green background color */
        color: white;
        border: none;
        cursor: pointer;
    }}
</style>
"""

# Render the HTML with CSS
st.markdown(html_code, unsafe_allow_html=True)

# Your Streamlit content here
st.markdown("""<h1 style="color: white;">A Computer Engineer Student's Blog</h1>""",unsafe_allow_html=True)

# Assets Loader
image_path1= "images/Streamlit_Img.jpg"
image_path2= "images/HPPY.jpg"


with st.container():
    st.write("-----")

    # Specify the number of columns you want
    first_column, second_column = st.columns(2)

    with first_column:
        st.markdown("""<h1 style="color: white;">I'm Dyna Pajo Buna</h1>""",unsafe_allow_html=True)
        st.markdown("""<h1 style="color: white;">Explore the World of Computer Engineering through my Blog!</h1>""",unsafe_allow_html=True)

    with second_column:

        st.markdown("""
                  

                  <a href>
                    <img src="https://scontent.fcgy1-1.fna.fbcdn.net/v/t1.15752-9/368059921_2269106506612968_1533353802663590241_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeF6UspmQQYZiYJ94ETefaGFG2q9LVikligbar0tWKSWKFPlZa1bf678K_n8NsUbVLYSkrD7dGLT_fcYoFeYiRZK&_nc_ohc=IRK5XdwhbbMAX-38GgV&_nc_ht=scontent.fcgy1-1.fna&oh=03_AdRm6Ndb4VbIf8ufS2JTf-VCimT8v-DxOgRH6w0BIhyagw&oe=65886764" width="400px";>
                    </a>
                  
                  
                  
                  
                  
                  """, unsafe_allow_html=True)

    

st.write("-----")



st.write("If you require assistance with any engineering-related inquiries, simply complete the provided form:")

contact_form = """
    <form action="https://dynabuna2@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

st.markdown(contact_form,unsafe_allow_html=True)

#Projects
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if os.path.exists(image_path1):
            IMG1 = Image.open(image_path1)
            st.image(IMG1)
        else:
            st.error(f"File '{image_path1}' not found. Please check the file path.")  
        
    with text_column:
        st.subheader("Challenges in Computer Engineering")
        st.write(
            """"
            Computer engineering students face a variety of challenges, including:

*Rapidly evolving technology
*High demand for skills
*Pressure to succeed
*Balancing coursework with other commitments
*Working long hours
*Dealing with stress
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if os.path.exists(image_path2):
            IMG2 = Image.open(image_path2)
            st.image(IMG2)
        else:
            st.error(f"File '{image_path2}' not found. Please check the file path.")
    with text_column:
        st.subheader("Happy")
        st.write(
            """
            Despite the challenges, computer engineering students find joy and satisfaction in their chosen field. Here are some reasons why computer engineering students are happy:

* Completing a difficult project
* Seeing their work used by others
* Receiving positive feedback from professors or employers
* Getting a job after graduation
* Solving a complex problem
* Making a breakthrough in their research
* Learning a new programming language
* Developing a new algorithm
* Designing a new product or system

These are just a few of the many things that make computer engineering students happy. If you are considering a career in computer engineering, I encourage you to learn more about this exciting and rewarding field.
            """
            
        )
