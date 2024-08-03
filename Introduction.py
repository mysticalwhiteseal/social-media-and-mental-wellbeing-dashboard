import streamlit as st
from PIL import Image
# import base64

st.set_page_config(
    page_icon="./images/happy.png",
    page_title="Introduction",
    layout="wide"
)

def crop_image(image):
    width, height = image.size
    if width == height:
        return image
    offset  = int(abs(height-width)/2)
    if width>height:
        image = image.crop([offset,0,width-offset,height])
    else:
        image = image.crop([0,offset,width,height-offset])
    return image

# Local GIF
# file_ = open("./images/think_spin.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

st.markdown("<h2 style='text-align: center;'>Social Media and Mental Well-Being</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>An interactive dashboard visualizing findings of the study, serving you insightful information on user demographics, online social activity, and emotional states.</p>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<p></p>", unsafe_allow_html=True)
_left, mid, _right = st.columns([0.38, 0.8, 0.2])
mid.image("./images/boo.jpg", width=600)
st.markdown("<p></p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.1, 0.3, 0.1])
col2.markdown("<h4 style='text-align: justify; line-height: 40px;'>Social media can be a wonderful tool, connecting individuals far apart together and keeping us in touch. But have you ever stopped and wondered: Is it really all rainbows and sunshine? Since the COVID-19 wave hit, for the first time, we experienced extended periods of isolation... relying heavily on social media to fill the void of physical interactions.</h4>", unsafe_allow_html=True)

st.markdown("###")
st.title("How can it possibly be bad?")
st.markdown("---")
# st.markdown(f"<img src=\"data:image/gif;base64,{data_url}\">", unsafe_allow_html=True)

img1_col1, img2_col2 = st.columns([1.5, 1])
img1_col1.markdown("![Alt Text](https://media.tenor.com/szH2qsISnzMAAAAi/emoji-thinking.gif)")
with img2_col2:
    st.markdown("<h4 style='text-align: justify; line-height: 40px;'>With more time spent online, the darker sides of social media started to become more apparent...</h4>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ff4949; text-align: center; line-height: 40px;'>The endless scrolling,</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>the <span style='color: #ff4949'>pressure</span> to stay constantly updated,</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>the <span style='color: #ff4949'>bottomless appetite</span> for <span style='color: #ff4949'>validation</span>,</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>instant gratification.</h3>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("<h3 style='text-align: center; line-height: 20px;'>The constant fidgeting</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 20px;'> waiting for something to happen.</h3>", unsafe_allow_html=True)
st.markdown("#####")
st.markdown("<p style='text-align: center; font-size: 60px; line-height: 90px;'>All for that Sweet, Sweet Dopamine Boost when Someone Double-Taps Your Post.</p>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; line-height: 20px;'>And guess what? They keep YOU coming back for more!</h4>", unsafe_allow_html=True)
st.markdown("#####")
img2_col1, img2_col2, img2_col3, img2_col4, img2_col5, img2_col6 = st.columns(6)

img2_col2.image("./images/Insta.svg", use_column_width=True)
img2_col3.image("./images/FB.png", use_column_width=True)
img2_col4.image("./images/Whatsapp.svg", use_column_width=True)
img2_col5.image("./images/Snapchat.svg", use_column_width=True)

st.markdown("#####")
img3_col1, img3_col2, img3_col3, img3_col4, img3_col5 = st.columns(5)

with img3_col2:
    st.markdown("#####")
    st.image("./images/Twitter_X.jpg", use_column_width=True)
img3_col3.image("./images/LinkedIn_logo.png", use_column_width=True)
img3_col4.image("./images/Telegram.svg", use_column_width=True)

st.markdown("#####")
st.title("Okay, but HOW BAD is it?")
st.markdown("<h4 style='text-align: justify; line-height: 40px;'>The effects of prolonged social media use can be quite significant, impacting various aspects of our lives.</h4>", unsafe_allow_html=True)

st.markdown("#")
img4_col1, img4_col2 = st.columns([1.3, 1])
with img4_col1:
    st.markdown("#")
    st.markdown("######")
    st.markdown("<h3 style='text-align: right; line-height: 40px;'>Constantly staring at highlights of other people's lives can make you feel inadequate. \'Compare and despair\', as they say, causes frequent mood swings, as you lament why nice things never ever happen to you.</h3>", unsafe_allow_html=True)

img4_col2.image("./images/mood_swing.jpg", width=400)

st.markdown("#")
st.markdown("<h2 style='text-align: center; line-height: 40px;'>You may lose sleep if you only fall asleep to screens, your sleep quality and cycles utterly in shambles.</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; line-height: 40px;'>Being sedentary doesn't sound all that bad, until it hits you with health problems. Obesity, cardiovascular disease, poor posture, to name a few.</h2>", unsafe_allow_html=True)

st.markdown("#")
st.markdown("##")
img5_col1, img5_col2 = st.columns([1, 1.3])

img5_col1.image("./images/distracted.jfif", caption="Vecteezy.com")

with img5_col2:
    st.markdown("####")
    st.markdown("<h3 style='text-align: right; line-height: 40px;'>If you are addicated enough, you can be easily distracted from what you were supposed to be doing. Productivity goes out the window when your attention is fragmented, stolen by those</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 100px; line-height: 100px; color: yellow;'><b>DING,</b></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 100px; line-height: 90px; color: yellow;'><b>DING,</b></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 100px; line-height: 90px;'><span style='color: yellow;'><b>DING!</b></span>s</h1>", unsafe_allow_html=True)

st.markdown("##")
img6_col1, img6_col2 = st.columns([1.3, 1])


with img6_col1:
    st.markdown("")    
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>Endlessly chasing likes, comments, and followers can become an unhealthy obssession.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>Your self worth now tied to these virtual assets.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>The pressure to always maintain a PERFECT image online. That distorted, unrealistic, idealized portrayal of life, unattainable without significant stress.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; line-height: 40px;'>Not to mention the exposure of negativity and cyberbullying the longer we spend online.</h3>", unsafe_allow_html=True)

img6_col2.image("./images/self_esteem.jpg", caption="Vecteezy.com", width=650)

st.markdown("###")
st.title("Are we screwed?")
st.markdown("---")
st.markdown("<h3 style='text-align: left; line-height: 40px;'>Of course, if you are not glued to devices all day, you're probably fine.</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; line-height: 40px;'>Moderation is key, the excessive use of anything is going to backfire. When you have a healthy balance of entertainment and the rest of your life, these effects would not apply to you.</h3>", unsafe_allow_html=True)
st.markdown("###")

img7_col1, img7_col2 = st.columns([1, 1.3])

img7_col1.image("./images/attack_on_socials.png", width=550)

with img7_col2:
    st.title("Let's Delve into The Labyrinth of Social Media and Mental Health Together!")
    st.subheader("with")

    eric = crop_image(Image.open("./images/Eric.JPG"))
    
    img8_col1, img8_col2, img8_col3 = st.columns([0.5, 0.2, 0.5])
    
    with img8_col1:
        st.image(eric, use_column_width=True)
        st.markdown("<p style='text-align: center; font-size: 20px;'>Eric Foo Zhi Xian</p>", unsafe_allow_html=True)
    with img8_col2:
        st.markdown("###")
        st.markdown("#####")
        st.markdown("<p style='text-align: center; font-size: 65px;'><b>&</b></p>", unsafe_allow_html=True)
    with img8_col3:
        st.image(eric, use_column_width=True)
        st.markdown("<p style='text-align: center; font-size: 20px;'>Eric Foo Zhi Xian</p>", unsafe_allow_html=True)
