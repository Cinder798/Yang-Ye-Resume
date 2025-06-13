import streamlit as st
import plotly.graph_objects as go
from wordcloud import WordCloud
from PIL import Image
st.set_page_config(page_title="Home", layout="wide")
st.sidebar.image("profile.jpg", width=150)
st.sidebar.markdown("## Ye Yang (Cinder)")
st.sidebar.markdown("🔍 NLP-focused Researcher & Communicator")
st.sidebar.markdown("📍 Malaysia | Harbin | Global")
st.sidebar.markdown("✉️ yangyemishi99@gmail.com")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")
st.title("🌸 Welcome to Ye Yang's Dynamic Resume")
st.markdown("_An NLP Research Enthusiast bridging cultures, codes, and cognition._")

st.subheader("🧠 My Comprehension of Linguistics")
st.image("My Comprehension of Linguistics.jpg", caption="A model connecting linguistic meaning, probability, and communication", use_column_width=True)

with st.expander("🧩 Explanation of the Linguistic Model (中英对照)", expanded=False):
    st.markdown("""
**Only Aim of Languages = To COMMUNICATE**  
Language = multiple parallel universes  
Language is subjective  
Inspired by Grice, Austin, Chomsky, and Lakoff, this thought model maps language onto probability events, where each utterance 'collapses' one possible universe.
> 语言的唯一目的 = 沟通  
语言是主观的、多重宇宙叠加的产物。每一句话都像量子坍缩，选定一个现实。
""")
skills = {
    'Python': 6,
    'NLP': 7,
    'Academic Writing': 8,
    'Discourse Analysis': 8,
    'Streamlit': 7,
    'Communication': 9,
}
categories = list(skills.keys())
values = list(skills.values()) + [skills[list(skills.keys())[0]]]
fig = go.Figure(data=[
    go.Scatterpolar(r=values, theta=categories + [categories[0]], fill='toself')
])
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,10])), showlegend=False, title="Skill Radar")
st.plotly_chart(fig, use_container_width=True)
st.subheader("☁️ Project Keywords")
text = "chatbot speech_act CDA pragmatics power emotion politeness cross_culture AI discourse perlocutionary linguistics"
wc = WordCloud(width=800, height=300, background_color='white').generate(text)
st.image(wc.to_array(), use_column_width=True)
