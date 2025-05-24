import re

SECTIONS = ["experience", "education", "skills", "projects", "certifications"]

def calculate_ats_score(resume_text, job_text, extracted_skills):
    """
    Calculate ATS score based on:
    - Skill match
    - Section presence
    - Formatting quality (basic check)
    - Keyword match

    Returns:
    - breakdown: dict of score components
    - matched_skills: list of matched skills
    """
    score = 0
    breakdown = {}

    # 1. Skill Match
    matched_skills = [skill for skill in extracted_skills if skill.lower() in job_text.lower()]
    skill_score = len(matched_skills) / max(len(extracted_skills), 1)
    score += skill_score * 40
    breakdown["Skill Match"] = round(skill_score * 40, 2)

    # 2. Section Presence
    section_score = sum(1 for section in SECTIONS if section in resume_text.lower()) / len(SECTIONS)
    score += section_score * 15
    breakdown["Section Coverage"] = round(section_score * 15, 2)

    # 3. Formatting Quality (Basic check)
    formatting_score = 10 if len(resume_text.split()) > 100 else 5
    score += formatting_score
    breakdown["Formatting Quality"] = formatting_score

    # 4. Keyword Match
    jd_keywords = re.findall(r'\b\w+\b', job_text.lower())
    resume_words = re.findall(r'\b\w+\b', resume_text.lower())
    common_keywords = set(jd_keywords).intersection(set(resume_words))
    keyword_score = len(common_keywords) / max(len(jd_keywords), 1)
    score += keyword_score * 20
    breakdown["Keyword Match"] = round(keyword_score * 20, 2)

    # Final Score
    breakdown["Total ATS Score"] = round(score, 2)

    return breakdown, matched_skills
