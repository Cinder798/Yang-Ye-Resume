import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Radar Skill Animation", layout="wide")
st.title("📊 Dynamic Skill Radar")
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
    title: {
      text: 'Skill Radar (Animated)',
      textStyle: { fontSize: 20 }
    },
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
      splitArea: {
        areaStyle: {
          color: ['#f5f5f5', '#fff']
        }
      },
      axisLine: {
        lineStyle: { color: 'gray' }
      }
    },
    series: [{
      name: 'Skill Level',
      type: 'radar',
      data: [{
        value: [8, 9, 9, 8, 7, 9],
        name: 'Cinder',
        areaStyle: { opacity: 0.3 }
      }],
      animationDuration: 1000,
      animationEasing: 'elasticOut'
    }]
  };
  function animateRadar() {
    let base = [8, 9, 9, 8, 7, 9];
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
