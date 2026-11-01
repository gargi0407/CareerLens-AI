import re

def normalize(text):
    return re.sub(r"[^a-z0-9+#. ]", " ", text.lower())

def analyze_resume(resume_text, required_skills):
    """Match a role's sample skills against the resume text."""
    content = normalize(resume_text)
    matched, missing = [], []
    for skill in required_skills:
        clean_skill = normalize(skill).strip()
        if clean_skill and clean_skill in content:
            matched.append(skill.strip())
        else:
            missing.append(skill.strip())
    score = round((len(matched) / len(required_skills)) * 100) if required_skills else 0
    return {"matched": matched, "missing": missing, "score": score}
