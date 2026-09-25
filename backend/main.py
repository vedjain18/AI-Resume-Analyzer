from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil

from backend.resume_parser import extract_resume_text
from backend.analyzer import analyze_resume
from backend.recommender import generate_recommendations

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze a resume against a job description.",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    file_path = f"temp_{resume.filename}"

    try:

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                resume.file,
                buffer
            )

        resume_text = extract_resume_text(
            file_path
        )

        result = analyze_resume(
            resume_text,
            job_description
        )

        recommendations = generate_recommendations(
            result["missing_skills"],
            result["matching_skills"],
            result["similarity_score"]
        )

        result["recommendations"] = recommendations

        return result

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)