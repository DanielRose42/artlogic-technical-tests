// Fetch FAQ questions from data in local JSON file
fetch("data.json")
    // Parse JSON data and convert to an array 
    .then(response => response.json())
    .then(data => {
        const jsonData = data["rows"];

        // Get FAQ container element
        const faq = document.getElementById("faq");

        // Loop through question data array
        for (let i = 0; i < jsonData.length; i++) {

            // Create outer question element
            let question = document.createElement("div");
            question.className = "question";

            // Create inner question text element
            let questionText = document.createElement("div");
            questionText.className = "question-text";

            // Add text from JSON data file
            questionText.innerHTML = (i + 1) + ". " + jsonData[i]["title"];

            // Append text element to question element and then append to faq
            question.appendChild(questionText);
            faq.appendChild(question);


            // Create outer answer element
            let answer = document.createElement("div");
            answer.className = "answer";

            // Create inner answer text element
            let answerText = document.createElement("div");
            answerText.className = "answer-text";

            // Add text from JSON data file
            answerText.innerHTML = jsonData[i]["content"];

            // Append text element to answer element and then append to faq
            answer.appendChild(answerText);
            faq.appendChild(answer);


            // Add a 'click' event listener to question element
            question.addEventListener("click", () => {

                // Toggle 'active' class to rotate triangle (right of question)
                question.classList.toggle("active");

                // On click, if answer element is not currently shown...
                if (!answer.style.maxHeight) {

                    // ...then reveal answer element
                    answer.style.maxHeight = answer.scrollHeight + "px";
                } else {
                    // ...or if answer element is currently shown then hide
                    answer.style.maxHeight = null;
                }
            });
        };
    })
    .catch(error => console.log(error));