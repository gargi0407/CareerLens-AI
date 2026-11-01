# CareerLens AI – Career & Skill Gap Analyzer

CareerLens AI is a beginner-friendly Python web application that helps students compare the skills mentioned in their resume with sample requirements for entry-level career roles.

## Features
- Upload a text-based PDF resume or paste resume text.
- Extract resume text using `pypdf`.
- Select a target role: Python Developer, AI/ML Intern, Web Developer or Data Analyst Intern.
- Identify skills found in the resume.
- Compare skills with a sample role checklist.
- Calculate an indicative skill alignment score.
- Generate a simple learning roadmap and next actions.
- Download a text report.

## Technology
Python, Streamlit, pypdf, basic text processing and rule-based skill matching.

## Run locally
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment (optional but recommended).
5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Start the app:

```bash
streamlit run app.py
```

## Deploy online with Streamlit Community Cloud
1. Create a GitHub repository named `CareerLens-AI`.
2. Upload all project files and folders.
3. Visit https://share.streamlit.io/ and sign in with GitHub.
4. Select **Create app** and choose your repository.
5. Set the main file path to `app.py`.
6. Click **Deploy**. Streamlit will provide a public app URL after deployment completes.

## Project workflow
Resume PDF / pasted text → text extraction → skill matching → role comparison → readiness indicator → learning roadmap.

## Important limitations
- This is an MVP using transparent, rule-based keyword matching. It does not currently use a Large Language Model or train a machine-learning model.
- The skill checklist is illustrative and should be adapted to real job descriptions.
- The readiness percentage is a simple skill-coverage indicator, not a prediction of employability or hiring success.
- Scanned/image-only PDFs may not contain extractable text; use a text-based PDF or paste the resume content.
- The application does not save uploaded resumes in a database.

## Future enhancements
- Integrate an LLM API for contextual resume feedback.
- Use NLP to recognize skill synonyms and context.
- Compare resumes against user-provided job descriptions.
- Add user accounts and saved progress with consent.
- Add interview question generation and project recommendations.

## Author
Student project – CareerLens AI
