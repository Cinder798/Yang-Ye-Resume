import streamlit as st
import plotly.graph_objects as go
from wordcloud import WordCloud
from PIL import Image

st.set_page_config(page_title="Home", layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Times New Roman', Times;
}
h1 {
  font-size: 16px;
  font-weight: bold;
  line-height: 1.5;
}
h2 {
  font-size: 14px;
  font-weight: bold;
  line-height: 1.5;
}
h3 {
  font-size: 12px;
  font-style: italic, bold;
  font-weight: bold;
  line-height: 1.5;
}
h4 {
  font-size: 10px;
  font-style: italic;
  line-height: 1.5;
}
p, li, div {
  font-size: 10px;
  font-style: none;
  line-height: 1.3;
}
[data-testid="stSidebar"] {
    background-color: rgba(230, 245, 227, 0.85);
    text-align: center;
}
[data-testid="stSidebar"] img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.image("profile.jpg", width=100)
st.sidebar.markdown("# Ye Yang (Cinder)")
st.sidebar.markdown("Academic BG: MELS, UM, Malaysia")
st.sidebar.markdown("🔍 Career Objective: NLP-focused Research Assistant")
st.sidebar.markdown("📍 Germany | Malaysia | Global")
st.sidebar.markdown("✉️ [Contact me] yangyemishi99@gmail.com")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")
st.sidebar.markdown("😼[My NLP Model-CC Kitty](https://6p8qtwfeqmwsvarblnx67m.streamlit.app/)")

st.markdown("## 🌸 Welcome to Ye Yang's Dynamic Resume")
st.markdown("*'Only THE ONE exists over time. 在无穷中，仅一息尚存，其余皆溃败于时间.——  An NLP Research Enthusiast bridging cultures, codes, and cognition.'*")

st.markdown("### 👑 Education & Work")
st.markdown("""
- **Master of English Language Studies**, University of Malaya, Malaysia  
  *Sep 2023 – Jul 2025* | CGPA: 3.53  
  Thesis: *Analysing Power Delegation in Food Persuasion through Perlocutionary Acts*  
- **Bachelor of Arts in English**, Xi’an Shiyou University, China  
  *Sep 2017 – Jun 2021* | Average: 87/100  
- **Summer School**, University of Birmingham (UK)
""")

st.markdown("### 🧠 My Comprehension of Linguistics")
st.image("My Comprehension of Linguistics.jpg", caption="A model connecting linguistic meaning, probability, and communication", use_column_width=True)

st.markdown("### 🧱 Skills & Projects")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📊 Skill Radar")
    iframe("https://cinder798.github.io/Yang-Ye-Resume/animated_radar_v5.html", height=520)
with col2:
    st.markdown("### ☁️ Project")
    st. markdown("Emotional AI Model--CC Kitty \nhttps://6p8qtwfeqmwsvarblnx67m.streamlit.app/")
    text = "chatbot speech_act CDA pragmatics power emotion politeness cross_culture AI discourse perlocutionary linguistics"
    wc = WordCloud(width=300, height=420, background_color='white').generate(text)
    st.image(wc.to_array(), use_column_width=True)

st.markdown("---")
st.markdown("Crafted with ❤️ by Cinder using Streamlit")
