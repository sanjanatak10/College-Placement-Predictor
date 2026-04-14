import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Placement Predictor", layout="wide")

# =========================
# CUSTOM CSS (MODERN UI)
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
}

h1, h2, h3 {
    color: white;
}

.stButton>button {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 16px;
    border: none;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODELS
# =========================
model = joblib.load("models/placement_model.pkl")
model_salary = joblib.load("models/salary_model.pkl")
features = joblib.load("models/features.pkl")

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div style="
background: linear-gradient(90deg,#1e3a8a,#06b6d4);
padding:30px;
border-radius:15px;
text-align:center;
margin-top:20px;
">
<h1 style="color:white;">🎓 AI Placement Predictor</h1>
<p style="color:white;">Fill in your details and predict your placement chances</p>
</div>
""", unsafe_allow_html=True)

# =========================
# INPUT SECTION
# =========================
col1, col2 = st.columns(2)

with col1:
    cgpa = st.slider("📘 CGPA", 0.0, 10.0, 7.0)
    internships = st.number_input("💼 Internships", 0, 10, 1)
    backlogs = st.number_input("⚠️ Backlogs", 0, 10, 0)

with col2:
    projects = st.number_input("📂 Projects", 0, 10, 2)
    mock_score = st.slider("🧠 Mock Interview Score", 0.0, 10.0, 5.0)
    skills = st.slider("💻 Skills (Python, DSA, ML)", 0, 10, 5)

# =========================
# CREATE INPUT DATA
# =========================
input_dict = {
    'cgpa': cgpa,
    'internships': internships,
    'projects': projects,
    'mock_interview_score': mock_score,
    'backlogs': backlogs,
    'skills_score': skills
}

# Reindex to exactly match training feature names and order, fill missing with 0
input_df = pd.DataFrame([input_dict]).reindex(columns=features, fill_value=0)

# =========================
# PREDICT BUTTON
# =========================
if st.button("🚀 Predict My Placement"):

    # Prediction
    prob = model.predict_proba(input_df)[0][1]
    salary = model_salary.predict(input_df)[0]

    prob_percent = round(prob * 100, 2)

    # RESULT UI
    st.markdown(f"""
    <div style="
    background: linear-gradient(90deg,#1e3a8a,#06b6d4);
    padding:30px;
    border-radius:15px;
    text-align:center;
    margin-top:20px;
    ">
    <h1 style="font-size:50px; color:white;">{prob_percent}%</h1>
    <p style="color:white;">Placement Chance</p>
    </div>
    """, unsafe_allow_html=True)

    # RESULT HEADER
    if prob > 0.7:
        st.success("🔥 High chances of placement")
    elif prob > 0.4:
        st.warning("⚠️ Moderate chances of placement")
    else:
        st.error("❌ Low chances of placement")

    # SCORE CARD
    st.markdown(f"""
    <div class="card">
        <h2>📊 Placement Probability</h2>
        <h1 style='color:#22c55e'>{prob_percent}%</h1>
    </div>
    """, unsafe_allow_html=True)

    # SALARY CARD
    st.markdown(f"""
    <div class="card">
        <h2>💰 Expected Salary</h2>
        <h1 style='color:#38bdf8'>₹{round(salary, 2)} LPA</h1>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # AI ANALYSIS REPORT
    # =========================
    st.markdown("### 🧠 AI Analysis Report")

    if prob > 0.7:
        st.success("You have a strong profile. Keep improving skills for top companies.")
    elif prob > 0.4:
        st.warning("Your profile is decent but needs improvement in key areas.")
    else:
        st.error("You need serious improvement to increase placement chances.")

    # =========================
    # PLOTLY CHART
    # =========================
    st.markdown("### 📊 Placement Probability Breakdown")

    probs = model.predict_proba(input_df)[0]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Not Placed", "Placed"],
        y=probs,
        marker_color=["#ef4444", "#22c55e"]
    ))
    fig.update_layout(
        plot_bgcolor="#0f172a",
        paper_bgcolor="#0f172a",
        font=dict(color="white"),
        title="Placement Prediction Breakdown"
    )
    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # PERSONALIZED ROADMAP
    # =========================
    st.markdown("### 🎯 Personalized Roadmap")

    if cgpa < 7:
        st.warning("📘 Improve CGPA to 7.5+")

    if internships < 1:
        st.warning("💼 Do at least 1 internship")

    if projects < 2:
        st.warning("📂 Build 2–3 strong projects")

    if skills < 6:
        st.warning("💻 Focus on DSA + Development")

    if mock_score < 5:
        st.warning("🧠 Practice mock interviews")