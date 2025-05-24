# app.py
import streamlit as st
from resume_parser import extract_text_from_pdf
from ats_score import calculate_ats_score
from skill_matcher import extract_skills, semantic_similarity

st.set_page_config(page_title="AI Resume ATS Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & ATS Score Predictor")
st.markdown("Upload your resume and paste a job description to get an ATS score and match percentage.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(resume_text)
        ats_breakdown, matched_skills = calculate_ats_score(resume_text, job_description, skills)
        similarity = semantic_similarity(resume_text, job_description)

    st.subheader("✅ ATS Score Breakdown")
    for key, value in ats_breakdown.items():
        st.write(f"**{key}**: {value}%")
    st.progress(min(100, int(ats_breakdown['Total ATS Score'])))

    st.subheader("🔍 Job Match Similarity")
    st.metric("Semantic Match", f"{similarity}%")

    st.subheader("💡 Skills Extracted from Resume")
    st.write(", ".join(skills))

    st.subheader("🧩 Skills Matched with Job Description")
    st.write(", ".join(matched_skills))

    st.success("Analysis complete! 🚀")
else:
    st.info("Upload a resume and paste a job description to begin.")
