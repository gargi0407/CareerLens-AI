import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_analyzer import analyze_resume
from career_recommender import get_learning_roadmap

st.set_page_config(page_title="CareerLens AI", page_icon="🎯", layout="wide")

st.markdown("""
<style>
.main {background-color: #f7f8fc;}
.hero {padding: 1.4rem 1.6rem; border-radius: 18px; background: linear-gradient(120deg,#243b80,#6b5bd2); color: white;}
.hero h1 {color:white; margin-bottom: .25rem;}
.hero p {color:#edf0ff; font-size:1.05rem;}
div[data-testid="stMetric"] {background:white; padding:16px; border-radius:14px; border:1px solid #e8eaf4;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🎯 CareerLens AI</h1>
<p>Discover your potential. Analyze your skills. Build your career.</p>
</div>
""", unsafe_allow_html=True)
st.write("An easy-to-use career readiness prototype that analyzes resume skills against entry-level job roles.")

roles = {
    "Python Developer": {
        "required": ["Python", "OOP", "SQL", "Git", " problem solving", " APIs", "Flask", "Django"],
        "roadmap": ["Revise Python fundamentals and OOP", "Practice SQL queries and database design", "Learn REST APIs and Flask or Django", "Build and publish a Python web application", "Practice coding interview problems"]
    },
    "AI / ML Intern": {
        "required": ["Python", "NumPy", "Pandas", "Machine Learning", "Statistics", "SQL", "Git", "Data Visualization"],
        "roadmap": ["Strengthen Python, NumPy and Pandas", "Learn statistics and data cleaning", "Study supervised and unsupervised learning", "Build a small prediction project", "Document experiments and publish on GitHub"]
    },
    "Web Developer": {
        "required": ["HTML", "CSS", "JavaScript", "PHP", "MySQL", "Git", "Responsive Design", "APIs"],
        "roadmap": ["Build responsive pages with HTML and CSS", "Practice JavaScript fundamentals", "Create CRUD applications with PHP and MySQL", "Learn API integration", "Deploy a complete web project"]
    },
    "Data Analyst Intern": {
        "required": ["Python", "SQL", "Excel", "Pandas", "Data Visualization", "Statistics", "Power BI"],
        "roadmap": ["Practice Excel and SQL", "Learn Python data analysis with Pandas", "Understand descriptive statistics", "Create charts and a dashboard", "Publish a data analysis case study"]
    }
}

with st.sidebar:
    st.header("⚙️ Career settings")
    target_role = st.selectbox("Choose your target role", list(roles.keys()))
    st.caption("Tip: Choose the role you want to prepare for, not necessarily your current job title.")
    st.markdown("---")
    st.write("**How it works**")
    st.write("1. Upload a PDF resume")
    st.write("2. Extract skills")
    st.write("3. Compare with role requirements")
    st.write("4. Review your improvement plan")

left, right = st.columns([1.15, 0.85], gap="large")
with left:
    st.subheader("📄 Upload your resume")
    uploaded = st.file_uploader("Choose a PDF resume", type=["pdf"])
    pasted_text = st.text_area("Or paste resume text here", height=150, placeholder="Paste your education, skills, projects and experience...")
    analyze = st.button("✨ Analyze my career readiness", type="primary", use_container_width=True)

with right:
    st.subheader("💡 About CareerLens")
    st.info("CareerLens is a student-focused prototype. It identifies skills mentioned in your resume and compares them with a selected role's sample skill checklist.")
    st.warning("The readiness score is an indicative checklist score, not a hiring prediction or professional assessment.")

if analyze:
    resume_text = pasted_text.strip()
    if uploaded is not None:
        try:
            resume_text = extract_text_from_pdf(uploaded)
        except Exception as e:
            st.error(f"Could not read this PDF: {e}")
    if not resume_text:
        st.error("Please upload a text-based PDF or paste your resume text first.")
    else:
        result = analyze_resume(resume_text, roles[target_role]["required"])
        st.markdown("---")
        st.header("📊 Your CareerLens report")
        m1, m2, m3 = st.columns(3)
        m1.metric("Placement readiness", f"{result['score']}%")
        m2.metric("Skills found", len(result["matched"]))
        m3.metric("Skills to develop", len(result["missing"]))

        st.subheader(f"🎯 Target role: {target_role}")
        st.progress(result["score"] / 100)
        if result["score"] >= 75:
            st.success("Good starting alignment. Strengthen your projects and practical experience.")
        elif result["score"] >= 40:
            st.info("You have a foundation. Focus on the missing skills and build evidence through projects.")
        else:
            st.warning("This role may require additional preparation. Follow the roadmap below.")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### ✅ Skills identified")
            if result["matched"]:
                for skill in result["matched"]:
                    st.write(f"• {skill}")
            else:
                st.write("No target skills identified yet.")
        with c2:
            st.markdown("#### 📌 Skills to improve")
            if result["missing"]:
                for skill in result["missing"]:
                    st.write(f"• {skill}")
            else:
                st.write("All sample checklist skills were found.")

        st.markdown("---")
        st.subheader("🗺️ Suggested learning roadmap")
        for i, item in enumerate(get_learning_roadmap(target_role, result["missing"], roles), 1):
            st.write(f"**Step {i}.** {item}")

        st.subheader("🚀 Recommended next actions")
        actions = []
        if result["missing"]:
            actions.append(f"Choose two missing skills to study first: {', '.join(result['missing'][:2])}.")
        actions += ["Add one practical project that demonstrates your skills.", "Update your resume with measurable project outcomes.", "Publish your code and a clear README on GitHub."]
        for action in actions:
            st.write(f"☐ {action}")

        report = f"""CAREERLENS AI - CAREER READINESS REPORT
Target role: {target_role}
Indicative readiness score: {result['score']}%
Skills identified: {', '.join(result['matched']) or 'None'}
Skills to improve: {', '.join(result['missing']) or 'None'}

Suggested next actions:
""" + "\n".join(f"- {x}" for x in actions)
        st.download_button("⬇️ Download text report", report, file_name="careerlens_report.txt")
        st.caption("Privacy note: This prototype processes the resume during the current session and does not save uploaded resume files to a database.")
else:
    st.markdown("---")
    st.subheader("Explore the sample roles")
    cols = st.columns(4)
    for col, role in zip(cols, roles.keys()):
        with col:
            st.markdown(f"**{role}**")
            st.caption(f"{len(roles[role]['required'])} sample skills")
