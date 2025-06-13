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

    Inspired by Grice, Austin, Chomsky, and Lakoff, this thought model maps language onto probability events, where each utterance 'collapses' one possible universe.  
    🗣️ “M lies on the bed” selects one reality.  
    💬 “I’m happy to talk to M.” expresses emotion → collapses a subjective state.
    """)

st.header("📊 Skill Radar – Breathing Animation")
echarts_code = """
<div id="main" style="width: 100%;height:500px;"></div>
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
<script>
var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
const base = [8, 9, 9, 8, 7, 9];
let scale = 1.0;
let direction = 0.005;
function getOption(values) {
  return {
    radar: {
      indicator: [
        { name: 'Python', max: 10 },
        { name: 'NLP', max: 10 },
        { name: 'Academic Writing', max: 10 },
        { name: 'Discourse Analysis', max: 10 },
        { name: 'Streamlit', max: 10 },
        { name: 'Communication', max: 10 }
      ]
    },
    series: [{
      type: 'radar',
      data: [{ value: values, areaStyle: {} }]
    }]
  };
}
function animate() {
  scale += direction;
  if (scale > 1.15 || scale < 0.85) direction *= -1;
  const newData = base.map(x => x * scale);
  myChart.setOption(getOption(newData));
}
myChart.setOption(getOption(base));
setInterval(animate, 80);
</script>
"""
st.components.v1.html(echarts_code, height=520)

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
let direction = 0.005;
setInterval(animate, 180);
echarts_code = """
<div id="main" style="width: 100%;height:500px;"></div>
<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
<script>
window.onload = function () {
    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);

    var base = [8, 9, 9, 8, 7, 9];
    var scale = 1.0;
    var direction = 0.005;

    function getOption(data) {
        return {
            radar: {
                indicator: [
                    { name: 'Python', max: 10 },
                    { name: 'NLP', max: 10 },
                    { name: 'Academic Writing', max: 10 },
                    { name: 'Discourse Analysis', max: 10 },
                    { name: 'Streamlit', max: 10 },
                    { name: 'Communication', max: 10 }
                ]
            },
            series: [{
                type: 'radar',
                data: [{ value: data, areaStyle: {} }]
            }]
        };
    }

    function updateChart() {
        scale += direction;
        if (scale >= 1.15 || scale <= 0.85) direction *= -1;
        var newData = base.map(x => Math.round(x * scale * 10) / 10);
        myChart.setOption(getOption(newData));
    }

    myChart.setOption(getOption(base));
    setInterval(updateChart, 100);
};
</script>
"""
st.components.v1.html(echarts_code, height=520)
from streamlit.components.v1 import iframe
iframe("https://cinder798.github.io/Yang-Ye-Resume/animated_radar.html", height=520)
