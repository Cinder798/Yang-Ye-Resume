import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objects as go
from wordcloud import WordCloud
from PIL import Image
import numpy as np
st.set_page_config(page_title="Cinder's Dynamic Resume", layout="wide")
st.sidebar.image("https://avatars.githubusercontent.com/u/134789802?s=400&u=fb3022d1d3e4f7f05c61d3f88fd771c4bbf25948", width=150)
st.sidebar.markdown("## Cinder (Ye Yang)")
st.sidebar.markdown("🔍 NLP-focused Researcher & Communicator")
st.sidebar.markdown("📍 Malaysia | Harbin | Global")
st.sidebar.markdown("✉️ yangye@email.com")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")
st.title("🌸 Welcome to Cinder's Dynamic Resume")
st.markdown("_An NLP Research Enthusiast bridging cultures, codes, and cognition._")
with st.expander("🧠 Linguistic Thought Map Summary"):
    st.markdown("""
    **Only Aim of Languages = To COMMUNICATE**  
    Language = multiple parallel universes  
    Language is subjective  
    \n
    Inspired by Grice, Austin, Chomsky, and Lakoff, this thought model maps language onto probability events, where each utterance 'collapses' one possible universe.  
    🗣️ “M lies on the bed” selects one reality.  
    💬 “I’m happy to talk to M.” expresses emotion → collapses a subjective state.
    """)
skills = {
    'Python': 8,
    'NLP': 9,
    'Academic Writing': 9,
    'Discourse Analysis': 8,
    'Streamlit': 7,
    'Communication': 9,
}
categories = list(skills.keys())
values = list(skills.values()) + [list(skills.values())[0]]
fig = go.Figure(data=[
    go.Scatterpolar(r=values, theta=categories + [categories[0]], fill='toself')
])
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,10])), showlegend=False, title="Skill Radar")
st.plotly_chart(fig, use_container_width=True)
st.subheader("☁️ Project Keywords")
text = "chatbot speech_act CDA pragmatics power emotion politeness cross_culture AI discourse perlocutionary linguistics"
wc = WordCloud(width=800, height=300, background_color='white').generate(text)
st.image(wc.to_array(), use_column_width=True)
st.subheader("🔬 Research Experience")
st.markdown("""
- **MA Thesis**: *Power Delegation in Aggressive Food Persuasion in Chinese Culture (UM, 2025)*  
- **Tools Used**: CDA, Speech Act Theory, Perlocutionary Acts, NVivo  
- **Focus**: How food-offering speech acts reveal implicit hierarchy and face negotiation in collectivist discourse
- **NLP Interest**: Mapping perlocutionary outcomes to computational models for emotion recognition.
""")
st.markdown("---")
st.markdown("Crafted with ❤️ by Cinder using Streamlit")
