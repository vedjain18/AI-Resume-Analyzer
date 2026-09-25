# AI Resume Analyzer

An AI-assisted resume analysis web application that compares a candidate's resume with a job description and provides a compatibility score, skill analysis, and recommendations.

## 🚀 Project Overview

The AI Resume Analyzer helps candidates understand how well their resume matches a particular job description.

The application:

- Accepts PDF and DOCX resumes
- Extracts text from the uploaded resume
- Detects technical skills
- Compares resume content with the job description
- Calculates text similarity using TF-IDF and Cosine Similarity
- Identifies matching and missing skills
- Generates resume improvement recommendations
- Displays the analysis through a simple web interface

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- PyMuPDF
- python-docx
- Scikit-learn

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning / NLP
- TF-IDF Vectorization
- Cosine Similarity
- Rule-based Technical Skill Extraction

## 🏗️ Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── main.py
│   ├── recommender.py
│   ├── resume_parser.py
│   └── skills.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── README.md
├── requirements.txt
└── resume_demo.docx
