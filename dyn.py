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
IMG1= Image.open("images/Streamlit_Img.jpg")
IMG2= Image.open("images/hppy.jpg")



with st.container():
    st.write("-----")

    # Specify the number of columns you want
    first_column, second_column = st.columns(2)

    with first_column:
        st.markdown("""<h1 style="color: white;">I'm Dyna Pajo Buna</h1>""",unsafe_allow_html=True)
        st.markdown("""<h1 style="color: white;">Explore the world of computer engineering through my blog!</h1>""",unsafe_allow_html=True)

    with second_column:

        st.markdown("""
                  

                  <a href>
                    <img src="https://scontent.fcgy1-1.fna.fbcdn.net/v/t1.15752-9/368059921_2269106506612968_1533353802663590241_n.png?_nc_cat=104&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeF6UspmQQYZiYJ94ETefaGFG2q9LVikligbar0tWKSWKFPlZa1bf678K_n8NsUbVLYSkrD7dGLT_fcYoFeYiRZK&_nc_ohc=IRK5XdwhbbMAX-38GgV&_nc_ht=scontent.fcgy1-1.fna&oh=03_AdRm6Ndb4VbIf8ufS2JTf-VCimT8v-DxOgRH6w0BIhyagw&oe=65886764" width="800px";>
                    </a>
                  
                  
                  
                  
                  
                  """, unsafe_allow_html=True)

    

st.write("-----")



st.write("Get in touch with me by filling out the form below:")

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
        st.image(IMG1)  
        
    with text_column:
        st.subheader("Challenges in Computer Engineering")
        st.write(
            """"
            Computer engineering students face a variety of challenges, including:

Rigorous coursework: Computer engineering is a demanding discipline that requires students to master a wide range of subjects, including mathematics, physics, computer science, and electrical engineering. This can be a lot of material to cover, and it can be difficult to keep up with the pace of the coursework.

Rapidly evolving technology: The field of computer engineering is constantly changing, and students need to be able to adapt to new technologies and trends. This can be a challenge, as it requires students to constantly learn new things.

High demand for skills: Computer engineers are in high demand, and employers are looking for students with a strong skill set. This means that students need to be able to apply their knowledge to real-world problems and demonstrate their ability to solve problems.

Pressure to succeed: Computer engineering is a competitive field, and students often feel pressure to succeed. This can lead to stress and anxiety, which can make it difficult to focus on their studies.

Balancing coursework with other commitments: Computer engineering students often have a lot of commitments, such as internships, research projects, and extracurricular activities. This can make it difficult to balance their coursework with their other commitments.

Finding a job after graduation: The job market for computer engineers is competitive, and it can be difficult for students to find a job after graduation. This is especially true for students who do not have a lot of experience.

Keeping up with the latest technology: The field of computer engineering is constantly changing, and it can be difficult for students to keep up with the latest technology. This can make it difficult to stay competitive in the job market.

Dealing with ethical considerations: Computer engineers often have to deal with ethical considerations, such as the privacy of data and the safety of users. This can be a challenging and complex issue.

Working long hours: Computer engineers often have to work long hours, especially when they are working on deadlines. This can be stressful and can lead to burnout.

Dealing with stress: Computer engineering is a demanding field, and students often experience a lot of stress. This can be caused by the rigorous coursework, the pressure to succeed, and the long hours that students often have to work.

Despite these challenges, computer engineering can be a rewarding and challenging career. Students who are successful in this field will be well-prepared for a variety of exciting career opportunities.
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(IMG2)
    with text_column:
        st.subheader("Happy")
        st.write(
            """
            Despite the challenges, computer engineering students find joy and satisfaction in their chosen field. Here are some reasons why computer engineering students are happy:

Solving complex problems: Computer engineering students enjoy the challenge of solving complex problems. They are often drawn to the field because they enjoy using their analytical and problem-solving skills to create new and innovative solutions.

Making a difference in the world: Computer engineers play a vital role in developing the technologies that we rely on every day. Students in this field are motivated by the knowledge that their work is making a positive impact on the world.

Being creative: Computer engineering is a creative field that allows students to use their imagination and ingenuity to design new products and systems. Students enjoy the process of brainstorming ideas, developing prototypes, and testing their creations.

Working in a collaborative environment: Computer engineers often work in teams with other engineers, designers, and programmers. Students enjoy the collaborative nature of the work and the opportunity to learn from and collaborate with others.

Having a high-demand skill set: Computer engineers are in high demand, and graduates of computer engineering programs typically have no trouble finding jobs after graduation. Students enjoy the security of knowing that they have a marketable skill set that is in demand by employers.

Being well-paid: Computer engineers are typically well-paid, and they can command high salaries. Students enjoy the financial security that comes with a career in computer engineering.

Having a variety of career opportunities: Computer engineers can work in a variety of industries, including technology, manufacturing, finance, and healthcare. Students enjoy the flexibility and variety that a career in computer engineering offers.

Learning new things all the time: The field of computer engineering is constantly changing, and students are always learning new things. Students enjoy the challenge of keeping up with the latest technology and trends.

Being part of a global community: Computer engineers are part of a global community of professionals who are working to solve the world's most pressing problems. Students enjoy the feeling of being connected to a larger community of professionals who share their passions and interests.

Overall, computer engineering students are happy because they are passionate about their work, they are making a difference in the world, and they are in high demand. They enjoy the challenge of solving complex problems, the creativity of designing new products, and the collaborative nature of the work. They are also well-paid, have a variety of career opportunities, and are always learning new things.

In addition to the reasons listed above, here are some specific examples of things that make computer engineering students happy:

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