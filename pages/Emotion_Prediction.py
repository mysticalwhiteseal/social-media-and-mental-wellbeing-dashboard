import streamlit as st
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.svm import SVC

st.set_page_config(
    page_icon="./images/anxious.png",
    page_title="Emotion Prediction",
    layout="wide"
)

# Import the SVM model
svm = joblib.load("./model/final_svm.pkl")

if 'prediction_title' not in st.session_state:
    st.session_state["prediction_title"] = "Prediction Time! What is Your Emotion if..."


title = st.title(st.session_state.prediction_title)
_left2, mid2, _right2 = st.columns([0.125, 0.1, 0.1])
emoji = mid2.empty()
emoji_title = st.empty()

def update_emoji_img(output):
    if output == "Happiness":
        st.session_state["emoji"] = "./images/happy.png"
        st.session_state["emoji_title"] = "HAPPINESS"
        st.session_state["emoji_title_color"] = "yellow"
    elif output == "Sadness":
        st.session_state["emoji"] = "./images/sad.png"
        st.session_state["emoji_title"] = "SADNESS"
        st.session_state["emoji_title_color"] = "cyan"
    elif output == "Anger":
        st.session_state["emoji"] = "./images/angry.png"
        st.session_state["emoji_title"] = "ANGER"
        st.session_state["emoji_title_color"] = "red"
    elif output == "Anxiety":
        st.session_state["emoji"] = "./images/anxious.png"
        st.session_state["emoji_title"] = "ANXIETY"
        st.session_state["emoji_title_color"] = "purple"
    elif output == "Boredom":
        st.session_state["emoji"] = "./images/bored.png"
        st.session_state["emoji_title"] = "BOREDOM"
        st.session_state["emoji_title_color"] = "brown"
    elif output == "Neutral":
        st.session_state["emoji"] = "./images/neutral.png"
        st.session_state["emoji_title"] = "NEUTRAL"
        st.session_state["emoji_title_color"] = "lightblue"

def update_prediction_titles():
    st.session_state["prediction_title"] = "Your Emotion is..."

def form_submitted():
    input_dictionary = {
        "Age": st.session_state.age, 
        "Gender": st.session_state.gender, 
        "Platform": st.session_state.platform, 
        "Daily_Usage_Time (minutes)": st.session_state.daily_usage_time, 
        "Posts_Per_Day": st.session_state.posts, 
        "Likes_Received_Per_Day": st.session_state.likes, 
        "Comments_Received_Per_Day": st.session_state.comments, 
        "Messages_Sent_Per_Day": st.session_state.messages
    }
    new_input = pd.DataFrame(input_dictionary, index=[0])
    output = svm.predict(new_input)
    update_emoji_img(output)
    st.session_state["prediction_title"] = "Your Emotion is..."
    # update_prediction_titles()
    st.balloons()


with st.form(key="prediction"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Your AGE is", min_value=0, max_value=110, value=27, step=1, key = "age")
    
    with col2:
        gender = st.selectbox("Your gender is ", ("Male", "Female", "Non-binary"), key = "gender")
    
    platform = st.selectbox("The platform you're using is ", ("Facebook", "Instagram", "LinkedIn", "Snapchat", "Telegram", "Twitter", "Whatsapp"), key = "platform")
    daily_usage_time = st.number_input("In minutes, every day, you use it for ", min_value=0.0, max_value=1440.0, value=96.0, step=0.1, key = "daily_usage_time")
    
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    with col3:
        posts_per_day = st.number_input("The number of posts you make daily is ", min_value=0, max_value=86400, value=3, step=1, key="posts")
    with col4:
        likes_received_per_day = st.number_input("The number of likes you receive in a day is ", min_value=0, max_value=9999999, value=40, step=1, key="likes")
    with col5:
        comments_received_per_day = st.number_input("The number of comments you receive in a day is ", min_value=0, max_value=9999999, value=16, step=1, key="comments")
    with col6:
        messages_sent_per_day = st.number_input("The number of messages you send in a day is ", min_value=0, max_value=86400, value=23, step=1, key="messages")
    
    submit_button = st.form_submit_button("Predict Emotion!", on_click=form_submitted)
    
    if "emoji" in st.session_state:
        emoji.image(st.session_state["emoji"], width=256)
    if "emoji_title" in st.session_state:
        emoji_title.markdown(f"<h1 style='text-align: center; color: {st.session_state.emoji_title_color};'>{st.session_state.emoji_title}</h1>", unsafe_allow_html=True)
    # if "prediction_title" in st.session_state:
    #     title.




