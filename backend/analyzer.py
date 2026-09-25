from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from backend.skills import extract_skills


def calculate_similarity(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return round(similarity[0][0] * 100, 2)


def analyze_resume(resume_text, job_description):

    similarity_score = calculate_similarity(
        resume_text,
        job_description
    )

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matching_skills = resume_skills.intersection(job_skills)

    missing_skills = job_skills - resume_skills

    resume_only_skills = resume_skills - job_skills

    if len(job_skills) > 0:
        skill_match_score = (
            len(matching_skills) / len(job_skills)
        ) * 100
    else:
        skill_match_score = 0

    match_score = (
        similarity_score * 0.4
        + skill_match_score * 0.6
    )

    return {
        "match_score": round(match_score, 2),
        "similarity_score": similarity_score,
        "skill_match_score": round(skill_match_score, 2),
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills),
        "resume_only_skills": sorted(resume_only_skills)
    }

if __name__ == "__main__":

    resume = """
    Python Developer

    Skills:
    Python
    FastAPI
    SQL
    MySQL
    Git
    GitHub
    Machine Learning
    """

    job_description = """
    We are looking for a Python Developer.

    Requirements:
    Python
    FastAPI
    SQL
    AWS
    Docker
    Machine Learning
    Git
    """

    result = analyze_resume(
        resume,
        job_description
    )

    print("\n----- RESUME ANALYSIS -----")
    print("Match Score:", result["match_score"])
    print("Similarity:", result["similarity_score"])
    print("Skill Match:", result["skill_match_score"])

    print("\nMatching Skills:")
    print(result["matching_skills"])

    print("\nMissing Skills:")
    print(result["missing_skills"])

    print("\nResume-only Skills:")
    print(result["resume_only_skills"])