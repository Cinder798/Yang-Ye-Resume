import streamlit as st
st.set_page_config(page_title="Projects", layout="wide")
st.title("💼 Featured Projects")
projects = [
    {
        "title": "MA Thesis – Aggressive Food Persuasion in Chinese Culture",
        "keywords": "CDA, Perlocutionary Act, Collectivist Culture",
        "summary": "Analysed how food-offering speech acts encode implicit hierarchy and face negotiation strategies in Chinese discourse.",
        "tech": "NVivo, Speech Act Theory",
        "result": "8,000-word Master's thesis with perlocution-based coding."
    },
    {
        "title": "cc kitty 😼 – Emotional Book of Answers (Streamlit App)",
        "keywords": "Emotion Recognition, Streamlit, Multilingual Prompting",
        "summary": "Designed an interactive emotional response assistant using rule-based sentiment cues and bilingual logic branches.",
        "tech": "Python, Streamlit, Regex, Conditional Flows",
        "result": "Web demo with responsive output based on user mood."
    },
    {
        "title": "Cross-Cultural NLP & Pragmatics Research Direction",
        "keywords": "Intercultural Communication, Pragmatic Shift, NLP Mapping",
        "summary": "Exploring the potential of mapping politeness strategies and perlocutionary outcomes to computational linguistic models.",
        "tech": "Discourse Analysis, Intercultural Pragmatics",
        "result": "Research in progress."
    },
    {
        "title": "[Coming Soon] Curriculum Design & Visualisation Projects",
        "keywords": "Teaching Aid, Data Visualisation, Pedagogy",
        "summary": "Reserved space for future projects related to EFL teaching design or discourse visualisation tools.",
        "tech": "-",
        "result": "In progress."
    },
]
for p in projects:
    st.markdown(f"### {p['title']}")
    st.markdown(f"**Keywords**: {p['keywords']}")
    st.markdown(f"**Summary**: {p['summary']}")
    st.markdown(f"**Tech Stack**: {p['tech']}")
    st.markdown(f"**Output**: {p['result']}")
    st.markdown("---")
