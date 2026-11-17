from flask import Flask, render_template, request

app = Flask(__name__)

questions = {
    "Python": [
        "What is Python?",
        "What are the features of Python?",
        "What is the difference between List and Tuple?",
        "What are Python data types?",
        "What is a Dictionary in Python?"
    ],
    "Java": [
        "What is Java?",
        "What are the features of Java?",
        "What is OOP?",
        "What is the difference between JDK and JRE?",
        "What is inheritance in Java?"
    ],
    "SQL": [
        "What is SQL?",
        "What is a Primary Key?",
        "What is a Foreign Key?",
        "What is the difference between DELETE and DROP?",
        "What is a JOIN in SQL?"
    ],
    "HR": [
        "Tell me about yourself.",
        "What are your strengths?",
        "What are your weaknesses?",
        "Why should we hire you?",
        "Where do you see yourself in five years?"
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard", methods=["POST"])
def dashboard():
    name = request.form.get("name")
    return render_template("dashboard.html", name=name)

@app.route("/interview/<category>")
def interview(category):
    if category not in questions:
        return "Invalid category"
    return render_template(
        "interview.html",
        category=category,
        questions=questions[category]
    )

@app.route("/submit", methods=["POST"])
def submit():
    category = request.form.get("category")
    answers = [
        request.form.get(f"answer{i}", "")
        for i in range(1, 6)
    ]

    score = sum(
        10 for answer in answers
        if len(answer.strip()) >= 20
    )

    if score >= 40:
        feedback = "Excellent! Keep improving your knowledge."
    elif score >= 20:
        feedback = "Good attempt! Practice more technical questions."
    else:
        feedback = "Keep learning and practice more."

    return render_template(
        "result.html",
        category=category,
        score=score,
        feedback=feedback
    )

if __name__ == "__main__":
    app.run(debug=True)