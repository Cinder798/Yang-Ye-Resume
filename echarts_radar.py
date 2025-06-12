import streamlit as st
import streamlit.components.v1 as components
from wordcloud import WordCloud
st.set_page_config(page_title="Radar Skill Animation", layout="wide")
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
html_string = """
<!DOCTYPE html>
<html style="height:100%">
<head>
  <meta charset="UTF-8">
  <title>Radar Chart</title>
</head>
<body style="height:100%;margin:0">
<div id="radar" style="height:100%"></div>
<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
<script>
  var chart = echarts.init(document.getElementById('radar'));
  var option = {
    title: { text: 'Skill Radar (Animated)', textStyle: { fontSize: 20 }},
    tooltip: {},
    radar: {
      indicator: [
        { name: 'Python', max: 10 },
        { name: 'NLP', max: 10 },
        { name: 'Academic Writing', max: 10 },
        { name: 'Discourse Analysis', max: 10 },
        { name: 'Streamlit', max: 10 },
        { name: 'Communication', max: 10 }
      ],
      shape: 'circle',
      splitNumber: 5,
      splitLine: {
        lineStyle: {
          color: ['rgba(114,172,209,0.1)', 'rgba(114,172,209,0.2)', 'rgba(114,172,209,0.4)', 'rgba(114,172,209,0.6)', 'rgba(114,172,209,0.8)', 'rgba(114,172,209,1)'].reverse()
        }
      },
      splitArea: { areaStyle: { color: ['#f5f5f5', '#fff'] }},
      axisLine: { lineStyle: { color: 'gray' }}
    },
    series: [{
      name: 'Skill Level',
      type: 'radar',
      data: [{
        value: [6, 7, 8, 8, 7, 9],
        name: 'Cinder',
        areaStyle: { opacity: 0.3 }
      }],
      animationDuration: 1000,
      animationEasing: 'elasticOut'
    }]
  };
  function animateRadar() {
    let base = [6, 7, 8, 8, 7, 9];
    setInterval(() => {
      const variation = base.map(v => v + (Math.random() * 0.2 - 0.1));
      option.series[0].data[0].value = variation;
      chart.setOption(option);
    }, 1000);
  }
  chart.setOption(option);
  animateRadar();
</script>
</body>
</html>
"""
components.html(html_string, height=600)
st.subheader("☁️ Project Keywords")
text = "chatbot speech_act CDA pragmatics power emotion politeness cross_culture AI discourse perlocutionary linguistics"
wc = WordCloud(width=800, height=300, background_color='white').generate(text)
st.image(wc.to_array(), use_column_width=True)
