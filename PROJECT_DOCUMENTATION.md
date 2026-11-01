# CareerLens AI – Project Documentation

## 1. Introduction
CareerLens AI is a student-focused career readiness prototype. It helps learners understand how the skills written in their resume compare with a selected entry-level job role.

## 2. Problem Statement
Students often find it difficult to identify which technical skills are relevant to a target job and what they should learn next. CareerLens provides a simple first-level analysis to make skill gaps easier to understand.

## 3. Objectives
- Accept a resume in PDF format or pasted text.
- Extract readable resume content.
- Identify selected skills mentioned in the resume.
- Compare those skills with a sample job-role checklist.
- Display an indicative skill alignment score.
- Recommend a learning roadmap.

## 4. Proposed Solution
The user selects a target role and uploads a resume. The application extracts text from the PDF, normalizes the text and checks whether each sample required skill appears. It displays matched skills, missing skills, a percentage score and a learning roadmap.

## 5. Technology Stack
- Python: application logic.
- Streamlit: interactive web interface.
- pypdf: PDF text extraction.
- Regular expressions: text normalization.
- GitHub: source-code hosting.
- Streamlit Community Cloud: online deployment.

## 6. Modules
1. `app.py`: user interface, input handling and report display.
2. `resume_parser.py`: extracts text from PDF files.
3. `skill_analyzer.py`: matches resume text against role skills and calculates the score.
4. `career_recommender.py`: prepares role-based learning steps.
5. `requirements.txt`: lists Python dependencies.

## 7. System Workflow
1. User opens CareerLens AI.
2. User chooses a target job role.
3. User uploads a PDF resume or pastes resume text.
4. The application extracts or reads the text.
5. The skill analyzer checks the sample role checklist.
6. The dashboard displays skills found, skill gaps and an indicative score.
7. The user reviews and downloads the report.

## 8. Expected Output
The application displays:
- Target job role.
- Indicative readiness percentage.
- Skills identified in the resume.
- Skills to improve.
- Suggested learning roadmap.
- Recommended next actions.

## 9. Limitations
The current version uses keyword-based matching and illustrative skill lists. It is not a trained AI model and does not make hiring predictions. Scanned PDFs may require OCR, which is not included. The application does not store uploaded resumes.

## 10. Future Scope
- LLM-based contextual resume analysis.
- Skill synonym recognition using NLP.
- Job description upload and comparison.
- Interview preparation question generation.
- User progress tracking with privacy controls.

## 11. Conclusion
CareerLens AI demonstrates how Python text processing and an interactive web interface can help students understand skill gaps and plan career development. It provides a foundation for future LLM and NLP enhancements.
