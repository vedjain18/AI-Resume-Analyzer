SKILLS = [
    # Programming
    "Python",
    "Java",
    "C++",
    "JavaScript",

    # Backend
    "FastAPI",
    "Flask",
    "Django",
    "REST API",

    # Database
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",

    # Cloud
    "AWS",
    "Azure",
    "Docker",

    # AI / Data
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Pandas",
    "NumPy",
    "Scikit-learn",

    # Testing
    "Selenium",
    "PyTest",
    "API Testing",
    "Manual Testing",

    # Tools
    "Git",
    "GitHub",
    "Postman"
]


def extract_skills(text):
    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills

if __name__ == "__main__":
    sample_text = """
    I am a Python developer with experience in FastAPI,
    SQL, MySQL, Git and GitHub.

    I have also worked on Machine Learning projects.
    """

    skills = extract_skills(sample_text)

    print("Detected Skills:")
    print(skills)