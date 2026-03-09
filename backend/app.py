import PyPDF2
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)


# -------- Resume Text Extraction --------
def extract_text(file):

    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


# -------- Similarity Calculation --------
def match_score(resume, job):

    text = [resume, job]

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(text)

    score = cosine_similarity(matrix[0:1], matrix[1:2])

    return score[0][0] * 100


# -------- API Route --------
@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    jobdesc = request.form["jobdesc"]

    resume_text = extract_text(resume)

    score = match_score(resume_text, jobdesc)

    return jsonify({"score": round(score, 2)})


# -------- Run Server --------
if __name__ == "__main__":
    app.run(debug=True, port=5002)