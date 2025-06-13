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
import streamlit as st
st.set_page_config(page_title="About Me", layout="wide")
if "lang" not in st.session_state:
    st.session_state.lang = "EN"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🌐 中文" if st.session_state.lang == "EN" else "🌍 English"):
        st.session_state.lang = "CN" if st.session_state.lang == "EN" else "EN"
with col2:
    theme_toggle = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
    st.session_state.dark_mode = theme_toggle
if st.session_state.dark_mode:
    st.markdown("""
        <style>
        body { background-color: #111; color: #eee; }
        .stApp { background-color: #111; }
        </style>
    """, unsafe_allow_html=True)
if st.session_state.lang == "EN":
    st.title("👩‍💼 About Me")
    st.markdown("""
### 🎓 Academic & Research Background
I hold a Master's degree in English Language Studies from the University of Malaya, where I specialized in discourse analysis and pragmatics. My thesis explored implicit power dynamics in Chinese food-offering discourse, applying perlocutionary acts to cultural persuasion.
### 🌏 Intercultural Experience
Born in Harbin, educated in China and Malaysia, I have lived in multilingual, multiethnic environments. This shaped my sensitivity to cultural nuances and made me an adaptive communicator across East Asian and global contexts.
### 🧠 Communication Style & Personality
MBTI: ENTJ (Empathic Commander)  
Fluent in bilingual academic and interpersonal settings. I bring structure, empathy, and cross-domain curiosity to both individual projects and team collaborations.
### 📜 Certifications & Qualifications
- TEFL (Teaching English as a Foreign Language)
- Diploma in Applied Psychology
- Putonghua Proficiency Certificate
- IELTS Overall Band 7.0 (Writing 6.0)
### 🧭 Career Aspiration
I'm seeking opportunities in NLP research, computational pragmatics, or cross-cultural communication design — particularly roles that blend analytical depth with social understanding. I'm also open to RA roles, interdisciplinary PhDs, or creative research collaborations.
""")
else:
    st.title("👩‍💼 关于我")
    st.markdown("""
### 🎓 学术与研究背景
我拥有马来亚大学英语语言研究硕士学位，专注于语篇分析与语用学。硕士论文研究中国文化中食物劝说话语的隐性权力结构，并结合 perlocutionary acts 进行编码分析。
### 🌏 跨文化经历
出生于哈尔滨，在中国与马来西亚接受教育，长期生活在多语、多族群文化环境中。这让我对语言与文化的敏感度极高，能够在中西语境中灵活切换并进行深层沟通。
### 🧠 沟通风格与人格特质
MBTI：ENTJ（富有共情力的指挥官）  
擅长中英双语学术与生活交流，逻辑清晰，具有强烈好奇心和结构化思维，适合跨领域合作。
### 📜 证书与资质
- TEFL 国际英语教学资格证
- 应用心理学专科文凭
- 普通话等级证书
- 雅思 7.0（写作 6.0）
### 🧭 职业目标
我正在寻找 NLP 研究、跨文化语用分析或交互设计等方向的职位，尤其是能将人文语言理解与计算语言学结合的跨界项目。同时也积极申请博士项目或 RA 岗位。
""")
st.markdown("_An NLP Research Enthusiast bridging cultures, codes, and cognition._")
st.subheader("🧠 My Comprehension of Linguistics")
st.image("My Comprehension of Linguistics.jpg", caption="A model connecting linguistic meaning, probability, and communication", use_column_width=True)
with st.expander("🧩 Explanation of the Linguistic Model (中英对照)", expanded=False):
    st.markdown("""
**Only Aim of Languages = To COMMUNICATE**  
Language = multiple parallel universes  
Language is subjective  
Inspired by Grice, Austin, Chomsky, and Lakoff, this thought model maps language onto probability events, where each utterance 'collapses' one possible universe.
Only THE ONE exists over time.
> 语言的唯一目的 = 沟通  
语言是主观的、多重宇宙叠加的产物。每一句话都像量子坍缩，选定一个现实。
无穷中，仅一息尚存，其余皆败于时间。
""")
from streamlit.components.v1 import iframe
iframe("https://yourusername.github.io/Yang-Ye-Resume/animated_radar_v6.html", height=130)

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
wc = WordCloud(width=400, height=30, background_color='white').generate(text)
st.image(wc.to_array(), use_column_width=True)
