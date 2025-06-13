import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.card import card
from streamlit_timeline import timeline
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
st.set_page_config(page_title="Ye Yang Resume", layout="wide")
with st.sidebar:
    image = Image.open("profile.jpg")
    st.image(image, width=160)
    st.markdown("""
    ### Ye Yang (Cinder)  
    Master of English Language Studies, UM, Malaysia  
    🔍 NLP-focused Researcher & Communicator  
    📍 Malaysia | Harbin | Global  
    ✉️ [yangyemishi99@gmail.com](mailto:yangyemishi99@gmail.com)  
    🔗 [LinkedIn](https://linkedin.com/in/yourprofile)  
    🐱 [My NLP Model – CC Kitty](https://yourlink.to/cckitty)
    """)
tabs = st.tabs(["🏠 Home", "👑 Education & Work", "💻 Projects", "📊 Skills", "☁️ Keywords", "📬 Contact"])
with tabs[0]:
    st.title("🌸 Welcome to Ye Yang's Dynamic Resume")
    st.write("An NLP Research Enthusiast bridging cultures, codes, and cognition.")
    st.header("🧠 My Comprehension of Linguistics")
    st.image("My Comprehension of Linguistics.jpg", caption="My comprehension of Linguistics", use_container_width=True)
with tabs[1]:
    st.header("👑 Education & Work")
    with st.container():
        st.subheader("⏳ Timeline View")
        timeline_data = {
            "title": {"text": {"headline": "Ye Yang's Education & Experience Timeline"}},
            "events": [
                {
                    "media": {"url": ""},
                    "start_date": {"year": "2023", "month": "9"},
                    "end_date": {"year": "2025", "month": "7"},
                    "text": {
                        "headline": "Master of English Language Studies",
                        "text": "University of Malaya, Malaysia<br>CGPA: 3.53<br>Thesis: Analysing Power Delegation in Food Persuasion"
                    }
                },
                {
                    "media": {"url": ""},
                    "start_date": {"year": "2017", "month": "9"},
                    "end_date": {"year": "2021", "month": "6"},
                    "text": {
                        "headline": "BA in English",
                        "text": "Xi’an Shiyou University, China<br>Average: 87/100"
                    }
                },
                {
                    "media": {"url": ""},
                    "start_date": {"year": "2024", "month": "3"},
                    "end_date": {"year": "2024", "month": "7"},
                    "text": {
                        "headline": "Content Intern",
                        "text": "ABC Communications Ltd., Malaysia<br>Duties: Localisation, Sentiment Analysis<br>Outcomes: +18% engagement"
                    }
                },
                {
                    "media": {"url": ""},
                    "start_date": {"year": "2020", "month": "7"},
                    "text": {
                        "headline": "Summer School",
                        "text": "University of Birmingham (UK)"
                    }
                }
            ]
        }
        timeline(json.dumps(timeline_data), height=600)
with tabs[2]:
    st.header("💻 Projects")
    st.markdown("""
    - **CC Kitty: Emotional Book of Answers** – Bilingual emotional support app built using Streamlit + emotion keyword analysis  
    - **Research Thesis** – Fieldwork + discourse coding + CDA on Chinese food persuasion  
    - **Annotation Tool (in progress)** – JSON-based Streamlit tool for perlocution outcome tagging
    """)
with tabs[3]:
    st.header("📊 Skill Radar – Animated with ECharts")
    echarts_code = '''
    <div id="radar" style="width: 100%;height:500px;"></div>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <script>
    var chartDom = document.getElementById('radar');
    var myChart = echarts.init(chartDom);
    var option;
    let value = 1;
    let direction = 0.05;
    const base = [8, 7, 6, 8, 6, 7];
    option = {
      title: { text: '' },
      radar: {
        indicator: [
          { name: 'Academic Writing', max: 10 },
          { name: 'NLP', max: 10 },
          { name: 'Python', max: 10 },
          { name: 'Communication', max: 10 },
          { name: 'Streamlit', max: 10 },
          { name: 'Discourse Analysis', max: 10 }
        ]
      },
      series: [{
        type: 'radar',
        data: [
          { value: base.map(v => v), areaStyle: {} }
        ]
      }]
    };
    function update() {
      value += direction;
      if (value >= 1.2 || value <= 0.8) direction *= -1;
      let newData = base.map(v => v * value);
      option.series[0].data[0].value = newData;
      myChart.setOption(option);
    }
    setInterval(update, 100);
    myChart.setOption(option);
    </script>
    '''
    html(echarts_code, height=520)
with tabs[4]:
    st.header("☁️ Project Keywords")
    keywords = "emotion power speech_act chatbot pragmatics CDA politeness perlocutionary cross_culture discourse AI linguistics"
    wordcloud = WordCloud(width=800, height=300, background_color='white').generate(keywords)
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wordcloud, interpolation='bilinear')
    ax_wc.axis("off")
    st.pyplot(fig_wc)
with tabs[5]:
    st.header("📬 Let’s Connect")
    st.write("I'm always open to research collaborations, tech-linguistic projects, or academic conversations. Feel free to reach out!")
    st.markdown("✉️ Email: [yangyemishi99@gmail.com](mailto:yangyemishi99@gmail.com)")
    st.markdown("🔗 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")
