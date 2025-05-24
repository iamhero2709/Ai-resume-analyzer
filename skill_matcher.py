# skill_matcher.py
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_similarity(resume_text, job_text):
    embeddings = model.encode([resume_text, job_text], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1]).item()
    return round(score * 100, 2)

def extract_skills(resume_text):
    common_skills = ['python', 'machine learning', 'excel', 'communication',
                     'sql', 'project management', 'deep learning', 'tensorflow',
                     'pytorch', 'react', 'nodejs', 'cloud', 'aws', 'docker']
    return [skill for skill in common_skills if skill.lower() in resume_text.lower()]
