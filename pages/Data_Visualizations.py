import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_icon="./images/sad.png",
    page_title="Social Media and Mental Health Analysis",
    layout="wide"
)

eda_data = pd.read_csv("./dataset/Clean_Social_Media_Mental_Health.csv")

st.markdown("<h2 style='text-align: center;'>Social Media and Mental Health Analysis</h2>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; font-size: 20px;'>This interactive dashboard visualizes findings of the study, serving you insightful information on user demographics, online social activity, and emotional states.</p>", unsafe_allow_html=True)
st.markdown("<p></p>", unsafe_allow_html=True)
_left, mid, _right = st.columns([0.38, 0.8, 0.2])
mid.image("./images/boo.jpg", width=600)
st.markdown("<p></p>", unsafe_allow_html=True)

topic_col1, topic_col2, topic_col3 = st.columns([0.2, 0.8, 0.2])

with topic_col2:
    st.markdown("<h2 style='text-align: center;'>Topics to Explore:</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>• What Are the Top User Emotions for Each Platform?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>• What Is the Online Activity of Angry Twitter Users Like?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>• Why Is LinkedIn Considered \"Boring\"?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>• Generation Z vs Millennials: How Do They Use Social Media?</p>", unsafe_allow_html=True)

st.markdown("<h1></h1>", unsafe_allow_html=True)

# --------- What Are the Top User Emotions for Each Platform ---------
# Top Emotions by Platform Comparison
st.markdown("<h5 style='color: grey; '>Note: Data used in this study is relevant up to 2024.</h5>", unsafe_allow_html=True)
st.title("What Are the Top User Emotions for Each Platform?")
st.markdown("---")

# Plots are displayed with images, ran out of time to tinker with tools
# Nevermind, found out how to plot the graph, yay
q1_col1, q1_col2 = st.columns([1.5,1])
with q1_col1:
    # st.image("./images/Top_Emo.png", width=700)
    emotion_colors = {
        'Happiness': 'yellow',
        'Anger': 'red',
        'Neutral': 'gray',
        'Anxiety': 'orange',
        'Boredom': 'blue',
        'Sadness': 'purple'
    }

    emotion_platform_counts = eda_data.groupby(['Platform', 'Dominant_Emotion']).size().unstack().fillna(0)
    emotion_platform_proportions = emotion_platform_counts.div(emotion_platform_counts.sum(axis=1), axis=0)

    fig1, ax1 = plt.subplots(figsize=(14, 10))
    ax1 = emotion_platform_proportions.plot(kind='bar', stacked=True, color=[emotion_colors[emotion] for emotion in emotion_platform_proportions.columns])
    plt.title('Top Emotions by Platform Comparison')
    plt.xlabel('Platform')
    plt.ylabel('Proportion of Users')
    plt.legend(title='Dominant Emotion', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(ax1.figure)
with q1_col2:
    st.markdown("#")
    st.markdown("<h4 style='line-height: 40px;'>We find that <u>LinkedIn</u> stands out with the HIGHEST proportion of users experiencing BOREDOM.</h5>", unsafe_allow_html=True)
    st.markdown("<h4 style='line-height: 40px;'>In contrast, <u>Instagram</u> has the most users feeling HAPPINESS, while MOST <u>Twitter</u> users are SAD and ANGRY.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='color: lightgrey; line-height: 40px;'>But this begs the question: </h5> <h1 style='text-align: center;'>WHY?</h1>", unsafe_allow_html=True)



# --------- What Is the Online Activity of Angry Twitter Users Like ---------
# Distribution of Activities for Twitter Users Experiencing Anger - 4 subplots in total
st.markdown("#")
st.title("What Is the Online Activity of Angry Twitter Users Like?")
st.subheader("What made them tick?")
st.markdown("---")

# This one was easy to plot, so we plotted it, hooray
option = st.selectbox("Which to Investigate?", options=["How Many Posts Did They Make Per Day?", "How Many Likes Did They Receive Daily?", "How Many Comments Replied to Them Daily?", "How Many Messages Did They Send Per Day?"])
q2_col1, q2_col2 = st.columns([1, 1.5])

if option == "How Many Posts Did They Make Per Day?":
    with q2_col1:
        st.markdown("#")
        st.markdown("<h4 style='text-align: center; line-height: 40px;'>We see that most of these ANGRY users posted around 4 times a day, with a smaller group of them posting around 3 or 6 times per day.</h5>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: right; line-height: 40px;'>This high frequency of posting indicate that they are actively engaged...</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='line-height: 40px;'>...possibly involved in heated discussions or debates!</h4>", unsafe_allow_html=True)

    with q2_col2:
        # Filter the dataset for Twitter users experiencing Anger
        twitter_anger_data = eda_data[(eda_data['Platform'] == 'Twitter') & (eda_data['Dominant_Emotion'] == 'Anger')]

        # Plot the distributions for the specified columns
        fig2, ax2 = plt.subplots(figsize=(14, 10))

        # Posts_Per_Day
        sns.histplot(twitter_anger_data['Posts_Per_Day'], bins=10, kde=True, ax=ax2, color='skyblue')
        ax2.set_title('Posts Made by Angry Twitter Users Per Day')
        ax2.set_xlabel('Posts Per Day')
        ax2.set_ylabel('Frequency')
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        st.pyplot(fig2)

elif option == "How Many Likes Did They Receive Daily?":
    with q2_col1:
        st.markdown("####")
        st.markdown("<h4 style='text-align: left; line-height: 40px;'>Most angry users received between 30 to 50 likes per day!\nThis indicates that their posts were gaining SIGNIFICANT attention.</h5>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; line-height: 40px;'>But, the high number of likes is a double-edged sword.</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='line-height: 40px;'>Sure, it is a form of validation, but the \'attention\' can also mean <u>negative attention</u> and <u>critical feedback</u>. Faced with such negative attention, those easily overwhelmed by their emotions could be left feeling angry and resentful.</h4>", unsafe_allow_html=True)
    with q2_col2:
        # Filter the dataset for Twitter users experiencing Anger
        twitter_anger_data = eda_data[(eda_data['Platform'] == 'Twitter') & (eda_data['Dominant_Emotion'] == 'Anger')]

        # Plot the distributions for the specified columns
        fig2, ax2 = plt.subplots(figsize=(14, 10))

        # Likes_Received_Per_Day
        sns.histplot(twitter_anger_data['Likes_Received_Per_Day'], bins=10, kde=True, ax=ax2, color='salmon')
        ax2.set_title('Likes Received by Angry Twitter Users Per Day')
        ax2.set_xlabel('Likes Received Per Day')
        ax2.set_ylabel('Frequency')
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        st.pyplot(fig2)

elif option == "How Many Comments Replied to Them Daily?":
    with q2_col1:
        st.markdown("#")
        st.markdown("###")
        st.markdown("<h4 style='text-align: center; line-height: 40px;'>They also received 18 to 20 comments a day, a relatively high volume of comments. This indicates active engagement, but can also expose users to more negative or argumentative interactions.</h5>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; line-height: 40px;'>Just thinking about joining another Twitter argument makes their blood boil, it seems.</h4>", unsafe_allow_html=True)
       
    with q2_col2:
        # Filter the dataset for Twitter users experiencing Anger
        twitter_anger_data = eda_data[(eda_data['Platform'] == 'Twitter') & (eda_data['Dominant_Emotion'] == 'Anger')]

        # Plot the distributions for the specified columns
        fig2, ax2 = plt.subplots(figsize=(14, 10))

        # Comments_Received_Per_Day
        sns.histplot(twitter_anger_data['Comments_Received_Per_Day'], bins=10, kde=True, ax=ax2, color='lightgreen')
        ax2.set_title('Comments Received by Angry Twitter Users Per Day')
        ax2.set_xlabel('Comments Received Per Day')
        ax2.set_ylabel('Frequency')
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        st.pyplot(fig2)

else:
    with q2_col1:
        st.markdown("##")
        st.markdown("<h4 style='text-align: center; line-height: 40px;'>Around 18 to 25 messages were sent on Twitter by angry Twitter users. DMs (Direct Messages) are a form of direct communication on Twitter, where two users engage in one-on-one interactions and discussions.</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: left; line-height: 40px;'>While it sounds normal to be DM'ing someone, but given they have felt angry due to sending a high number of messages... It seems they might have had <u>taken the heated exchanges to personal messages</u>.</h4>", unsafe_allow_html=True)

    with q2_col2:
        # Filter the dataset for Twitter users experiencing Anger
        twitter_anger_data = eda_data[(eda_data['Platform'] == 'Twitter') & (eda_data['Dominant_Emotion'] == 'Anger')]

        # Plot the distributions for the specified columns
        fig2, ax2 = plt.subplots(figsize=(14, 10))

        # Messages_Sent_Per_Day
        sns.histplot(twitter_anger_data['Messages_Sent_Per_Day'], bins=10, kde=True, ax=ax2, color='lightcoral')
        ax2.set_title('Messages Sent by Angry Twitter Users Per Day')
        ax2.set_xlabel('Messages Sent Per Day')
        ax2.set_ylabel('Frequency')
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        st.pyplot(fig2)

st.markdown("#####")
st.markdown("#####")
q2_1_col1, q2_1_col2 = st.columns([1.5, 1])

with q2_1_col2:
    st.title("PHEW!")
    st.markdown("#")
    st.markdown("<h5 style='text-align: left; line-height: 40px;'>There is no shortage of ire and resentment on Twitter, as it suggests. The combination of high interactions rates across posts, likes, comments, and messages means that these users were DEEPLY engaged in the platform's social dynamics.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left; line-height: 40px;'>Grappled with rage, the intense and confrontational nature of Twitter discussions they participate in could be a key factor in the prevalence of ANGER among these users.</h5>", unsafe_allow_html=True)
with q2_1_col1:
    # Filter the dataset for Twitter users experiencing Anger
    twitter_anger_data = eda_data[(eda_data['Platform'] == 'Twitter') & (eda_data['Dominant_Emotion'] == 'Anger')]

    # Plot the distributions for the specified columns
    fig3, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Posts_Per_Day
    sns.histplot(twitter_anger_data['Posts_Per_Day'], bins=10, kde=True, ax=axs[0, 0], color='skyblue')
    axs[0, 0].set_title('Posts Per Day')
    axs[0, 0].set_xlabel('Posts Per Day')
    axs[0, 0].set_ylabel('Frequency')

    # Likes_Received_Per_Day
    sns.histplot(twitter_anger_data['Likes_Received_Per_Day'], bins=10, kde=True, ax=axs[0, 1], color='salmon')
    axs[0, 1].set_title('Likes Received Per Day')
    axs[0, 1].set_xlabel('Likes Received Per Day')
    axs[0, 1].set_ylabel('Frequency')

    # Comments_Received_Per_Day
    sns.histplot(twitter_anger_data['Comments_Received_Per_Day'], bins=10, kde=True, ax=axs[1, 0], color='lightgreen')
    axs[1, 0].set_title('Comments Received Per Day')
    axs[1, 0].set_xlabel('Comments Received Per Day')
    axs[1, 0].set_ylabel('Frequency')

    # Messages_Sent_Per_Day
    sns.histplot(twitter_anger_data['Messages_Sent_Per_Day'], bins=10, kde=True, ax=axs[1, 1], color='lightcoral')
    axs[1, 1].set_title('Messages Sent Per Day')
    axs[1, 1].set_xlabel('Messages Sent Per Day')
    axs[1, 1].set_ylabel('Frequency')

    plt.suptitle('Distribution of Activities for Twitter Users Experiencing Anger', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(fig3)

st.markdown("###")
st.markdown("#####")
img1_col1, img1_col2 = st.columns(2)
with img1_col1:
    st.subheader("Even with the death of the bird we all know and love, the users there do not mess around...")
    img1_col1.image("./images/dead_bird.jpg", use_column_width=True)
with img1_col2:
    st.image("./images/musk.webp", use_column_width=True)
    st.subheader("Let's move on and take a look at LinkedIn.")

# --------- What Is the Online Activity of Angry Twitter Users Like ---------
# Distribution of Daily Usage Time Across Different Social Media Platforms
st.markdown("###")
st.markdown("###")
st.title("Why is LinkedIn Considered \'Boring\'?")
st.subheader("Too formal? Too corporate? What could it be?")
st.markdown("---")

q3_col1, q3_col2 = st.columns(2)

with q3_col1:
    fig4, ax4 = plt.subplots(figsize=(8, 6))
    ax4 = eda_data.boxplot(column='Daily_Usage_Time (minutes)', by='Platform', grid=True)
    plt.title('Distribution of Daily Usage Time Across Different Social Media Platforms')
    plt.xlabel('Platform')
    plt.ylabel('Daily Usage Time (minutes)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(ax4.figure)

with q3_col2:
    st.markdown("")
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>From the boxplot, we can find that LinkedIn users had the LOWEST <u>median daily usage time</u> of around 60 minutes, with quite a narrow range. People typically use it 45 minutes to 65 minutes.</h4>", unsafe_allow_html=True)
    st.markdown("###")
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>This is likely because: </h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left; line-height: 40px;'>&nbsp;&nbsp;&nbsp;&nbsp;○&nbsp;&nbsp;&nbsp;&nbsp;LinkedIn users are more action-oriented</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left; line-height: 40px;'>&nbsp;&nbsp;&nbsp;&nbsp;○&nbsp;&nbsp;&nbsp;&nbsp;LinkedIn users are more intentional with their use</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left; line-height: 40px;'>&nbsp;&nbsp;&nbsp;&nbsp;○&nbsp;&nbsp;&nbsp;&nbsp;LinkedIn users typically log in, get the info they need, then log out</h5>", unsafe_allow_html=True)

st.markdown("#")
img2_col1, img2_col2 = st.columns(2)

with img2_col1:
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>LinkedIn is more of a professional networking platform than how we see social media. The content is more career-focused, less personal, and entertaining. There, you will find</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; line-height: 5px;'>Networking posts, Job postings,</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; line-height: 5px;'>Company updates, Industry trends,</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; line-height: 5px;'>Educational content</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>Things are less personal, expressive, and leisure oriented there. As users focus more on work, posts are more informative, comments never stray from the topic.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 1px;'><u>LinkedIn's not a canvas for your quirks and personal hue.</u></h4>", unsafe_allow_html=True)

with img2_col2:
    st.image("./images/linkedin.webp", width=750)

st.markdown("###")
img3_col1, img3_col2 = st.columns(2)

with img3_col1:
    st.image("./images/linkedin_peeps.webp")

with img3_col2:
    st.markdown("###")
    st.markdown("<h4 style='text-align: center; line-height: 40px;'>Professional goals are prioritized by the user base, to make positive impressions, explore career opportunities, showcase their expertise...</h4>", unsafe_allow_html=True)
    st.markdown("###")
    st.markdown("<h4 style='text-align: center; line-height: 40px;'>Seeing the self-promotion, people not accustomed might feel that it's \'stiff\' or \'lacking in personality\', just a cardboard cutout.</h4>", unsafe_allow_html=True)
    st.markdown("###")
    st.markdown("<h4 style='text-align: center; line-height: 40px;'>The constant corporate tone can feel like a droning lecture... repetitive and dry, which can make people looking for more dynamic content feel bored.</h4>", unsafe_allow_html=True)

# --------- Generation Z vs Millennials: How Do They Use Social Media ---------
# Gen Z and Millennials: Platform Frequency and Mean Daily Usage Time
st.markdown("#")
st.title("Generation Z vs Millennials: How Do They Use Social Media?")
st.subheader("Generational Differences in Social Media Behavior")
st.markdown("---")
st.markdown("<h4 style='text-align: left; line-height: 40px;'>We will now look into the differences between Gen Z and Millennial users in their social media activity, starting with Gen Z.</h4>", unsafe_allow_html=True)

st.markdown("######")
# Plots are displayed with images, couldn't figure this one out
# This plot is more complex than usual, didn't know how to code it
# in the format that conforms to st's docs 
img3_col1, img3_col2 = st.columns([1.5, 1])

with img3_col1:
    st.image("./images/Gen_Z.png", width=700)

with img3_col2:
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>Gen Z's favorite social media platforms were <u>Facebook</u>, <u>Twitter</u>, and <u>Instagram</u>.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>While Telegram, Whatsapp, and LinkedIn were left in the dust, less popular amongst Gen Z users.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>Platforms with HIGHEST <u>daily usage time</u> were <u>Instagram</u> and <u>Snapchat</u>, while LinkedIn had the lowest daily usage time, only used briefly each day compared to other platforms.</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; line-height: 5px;'></h4>", unsafe_allow_html=True)

st.markdown("######")
st.markdown("<h4 style='text-align: left; line-height: 40px;'>How about Millennials?</h4>", unsafe_allow_html=True)

st.markdown("######")
img4_col1, img4_col2 = st.columns([1, 1])

with img4_col2:
    st.image("./images/Millennial.png", width=700)

with img4_col1:
    st.markdown("")
    st.markdown("<h4 style='text-align: right; line-height: 40px;'>Millennials prefer <u>Instagram</u>, <u>LinkedIn</u>, <u>Twitter</u>, and <u>Facebook</u>...</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>...over Telegram and Snapchat, which together only make up 14% of the usages.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>Platforms with HIGHEST <u>daily usage time</u> were <u>Instagram</u> and <u>Whatsapp</u>, while LinkedIn (again!) had the lowest daily usage time, only used for a mean of 56.79 minutes daily.</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; line-height: 40px;'>With the above, a few findings could be derived between Gen Z and Millennials.</h4>", unsafe_allow_html=True)

st.markdown("#")
st.markdown("#")
st.subheader("Side-by-Side Comparison: The FINAL Showdown", divider=True)
img5_col1, img5_col2 = st.columns([1, 1])

with img5_col1:
    st.image("./images/Gen_Z.png", width=700)

with img5_col2:
    st.image("./images/Millennial.png", width=700)

st.markdown("<h4 style='text-align: left; line-height: 40px;'>In comparison, LinkedIn was significantly less popular among Gen Z. This could be because Millennials are more likely to be established in their careers, making the work-focused platform more appealing and helpful to them.</h4>", unsafe_allow_html=True)
st.markdown("######")
st.markdown("<h4 style='text-align: right; line-height: 40px;'>Meanwhile, Gen Z users may still be educational phases or early career stages, naturally, there would be lower engagement rate with LinkedIn among all in the generation. In addition, Twitter (The single most controversial platform) also appears to be more popular among Gen Z, and Whatsapp being more likely to be used by Millennials.</h4>", unsafe_allow_html=True)
st.markdown("####")
st.markdown("<h4 style='text-align: left; line-height: 40px;'>The trends across social media usage are quite similar for both generations. <u>Instagram</u> particularly has the HIGHEST usage duration, its strong appeal and entertainment unmatched. Millennials tend to spend more time on Whatsapp on Gen Z, a difference in preference.</h4>", unsafe_allow_html=True)
st.markdown("######")
st.markdown("<h4 style='text-align: right; line-height: 40px;'>Another thing both Gen Z and Millennials can agree on is that: <u>LinkedIn</u> is used for the <u>least duration</u>. Its specific use case for professional purposes is consistent with our discoveries so far, standing strong with its principles from beginning to end.</h4>", unsafe_allow_html=True)


st.markdown("<h4 style='text-align: left; line-height: 40px;'></h4>", unsafe_allow_html=True)