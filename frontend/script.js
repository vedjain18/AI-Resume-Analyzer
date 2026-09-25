// ========================================
// GET HTML ELEMENTS
// ========================================

const resumeInput =
    document.getElementById("resume");

const fileName =
    document.getElementById("file-name");

const analyzeButton =
    document.getElementById("analyze-btn");

const loading =
    document.getElementById("loading");

const results =
    document.getElementById("results");

const inputSection =
    document.getElementById("input-section");

const resetButton =
    document.getElementById("reset-btn");


// ========================================
// RESUME FILE SELECTION
// ========================================

resumeInput.addEventListener(
    "change",
    function () {

        if (resumeInput.files.length > 0) {

            const selectedFile =
                resumeInput.files[0];

            fileName.textContent =
                selectedFile.name;

        } else {

            fileName.textContent =
                "No file selected";

        }

    }
);


// ========================================
// ANALYZE RESUME
// ========================================

analyzeButton.addEventListener(
    "click",
    async function () {

        // -------------------------------
        // GET INPUTS
        // -------------------------------

        const resume =
            resumeInput.files[0];

        const jobDescription =
            document
                .getElementById("job-description")
                .value
                .trim();


        // -------------------------------
        // VALIDATE RESUME
        // -------------------------------

        if (!resume) {

            alert(
                "Please select a PDF or DOCX resume."
            );

            return;

        }


        // -------------------------------
        // VALIDATE FILE TYPE
        // -------------------------------

        const fileNameLower =
            resume.name.toLowerCase();

        const validPDF =
            fileNameLower.endsWith(".pdf");

        const validDOCX =
            fileNameLower.endsWith(".docx");


        if (!validPDF && !validDOCX) {

            alert(
                "Please upload a PDF or DOCX file."
            );

            return;

        }


        // -------------------------------
        // VALIDATE JOB DESCRIPTION
        // -------------------------------

        if (!jobDescription) {

            alert(
                "Please enter the job description."
            );

            return;

        }


        // -------------------------------
        // CREATE FORM DATA
        // -------------------------------

        const formData =
            new FormData();


        formData.append(
            "resume",
            resume
        );


        formData.append(
            "job_description",
            jobDescription
        );


        // -------------------------------
        // SHOW LOADING
        // -------------------------------

        loading.classList.remove(
            "hidden"
        );

        results.classList.add(
            "hidden"
        );

        analyzeButton.disabled = true;

        analyzeButton.textContent =
            "⏳ Analyzing...";


        // -------------------------------
        // SEND TO FASTAPI
        // -------------------------------

        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/analyze",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            // ---------------------------
            // CHECK SERVER RESPONSE
            // ---------------------------

            if (!response.ok) {

                const errorText =
                    await response.text();

                console.error(
                    "Server error:",
                    errorText
                );

                throw new Error(
                    "Server could not analyze the resume."
                );

            }


            // ---------------------------
            // GET JSON RESULT
            // ---------------------------

            const data =
                await response.json();


            console.log(
                "Analysis result:",
                data
            );


            // ---------------------------
            // DISPLAY SCORES
            // ---------------------------

            document.getElementById(
                "match-score"
            ).textContent =
                `${data.match_score}%`;


            document.getElementById(
                "similarity-score"
            ).textContent =
                `${data.similarity_score}%`;


            document.getElementById(
                "skill-score"
            ).textContent =
                `${data.skill_match_score}%`;


            // ---------------------------
            // DISPLAY MATCHING SKILLS
            // ---------------------------

            displaySkills(
                "matching-skills",
                data.matching_skills
            );


            // ---------------------------
            // DISPLAY MISSING SKILLS
            // ---------------------------

            displaySkills(
                "missing-skills",
                data.missing_skills
            );


            // ---------------------------
            // DISPLAY RESUME-ONLY SKILLS
            // ---------------------------

            displaySkills(
                "resume-only-skills",
                data.resume_only_skills
            );


            // ---------------------------
            // DISPLAY RECOMMENDATIONS
            // ---------------------------

            displayRecommendations(
                data.recommendations
            );


            // ---------------------------
            // SHOW RESULTS
            // ---------------------------

            results.classList.remove(
                "hidden"
            );


            inputSection.classList.add(
                "hidden"
            );


            // Scroll to results

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });


        } catch (error) {

            console.error(
                "Analysis error:",
                error
            );


            alert(
                "Unable to analyze the resume.\n\n" +
                "Make sure FastAPI is running."
            );

        } finally {

            // ---------------------------
            // HIDE LOADING
            // ---------------------------

            loading.classList.add(
                "hidden"
            );


            analyzeButton.disabled =
                false;

            analyzeButton.textContent =
                "🚀 Analyze Resume";

        }

    }
);


// ========================================
// DISPLAY SKILLS
// ========================================

function displaySkills(
    elementId,
    skills
) {

    const container =
        document.getElementById(
            elementId
        );


    container.innerHTML = "";


    // No skills

    if (
        !skills ||
        skills.length === 0
    ) {

        const message =
            document.createElement(
                "span"
            );

        message.textContent =
            "None detected";

        message.style.color =
            "#64748b";

        container.appendChild(
            message
        );

        return;

    }


    // Create skill tags

    skills.forEach(
        function (skill) {

            const span =
                document.createElement(
                    "span"
                );


            span.className =
                "skill";


            span.textContent =
                skill;


            container.appendChild(
                span
            );

        }
    );

}


// ========================================
// DISPLAY RECOMMENDATIONS
// ========================================

function displayRecommendations(
    recommendations
) {

    const container =
        document.getElementById(
            "recommendations"
        );


    container.innerHTML = "";


    if (
        !recommendations ||
        recommendations.length === 0
    ) {

        const li =
            document.createElement(
                "li"
            );


        li.textContent =
            "No recommendations available.";


        container.appendChild(
            li
        );


        return;

    }


    recommendations.forEach(
        function (recommendation) {

            const li =
                document.createElement(
                    "li"
                );


            li.textContent =
                recommendation;


            container.appendChild(
                li
            );

        }
    );

}


// ========================================
// RESET / ANALYZE ANOTHER RESUME
// ========================================

resetButton.addEventListener(
    "click",
    function () {

        // Clear resume

        resumeInput.value = "";


        fileName.textContent =
            "No file selected";


        // Clear job description

        document.getElementById(
            "job-description"
        ).value = "";


        // Hide results

        results.classList.add(
            "hidden"
        );


        // Show input section

        inputSection.classList.remove(
            "hidden"
        );


        // Scroll to top

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    }
);