def generate_recommendations(
    missing_skills,
    matching_skills,
    similarity_score
):
    recommendations = []

    # Missing skills
    if missing_skills:
        skills = ", ".join(missing_skills)

        recommendations.append(
            f"Review the job requirements for these skills: {skills}. "
            "Only add them to your resume if you genuinely have the experience."
        )

    # Matching skills
    if matching_skills:
        recommendations.append(
            "Highlight your matching technical skills clearly "
            "in the Skills and Projects sections."
        )

    # Low text similarity
    if similarity_score < 50:
        recommendations.append(
            "Improve the alignment between your resume and the job "
            "description by emphasizing relevant experience and projects."
        )

    # Moderate text similarity
    elif similarity_score < 70:
        recommendations.append(
            "Consider using relevant terminology from the job description "
            "when it accurately describes your existing experience."
        )

    # Always useful
    recommendations.append(
        "Add measurable results and achievements to your project descriptions "
        "where possible."
    )

    return recommendations

if __name__ == "__main__":

    missing = ["AWS", "Docker"]

    matching = [
        "Python",
        "FastAPI",
        "SQL",
        "Git"
    ]

    similarity = 51.33

    recommendations = generate_recommendations(
        missing,
        matching,
        similarity
    )

    print("\n----- RECOMMENDATIONS -----")

    for number, recommendation in enumerate(
        recommendations,
        start=1
    ):
        print(f"{number}. {recommendation}")