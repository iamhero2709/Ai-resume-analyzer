# 📄 AI Resume Analyzer & ATS Score Predictor

Welcome to the **AI Resume Analyzer & ATS Score Predictor** — a smart web app designed to help job seekers improve their resumes by analyzing them against any job description. It provides an ATS (Applicant Tracking System) score breakdown and a semantic match percentage to predict how well your resume fits a specific job.

---

## 🔗 Live Demo

Try the app live here: [AI Resume Analyzer & ATS Score Predictor](https://airesumeanalyzerwithats.streamlit.app/)

---

## Features

- Upload your resume as a PDF file.
- Paste any job description to analyze.
- Get a detailed ATS score breakdown including:
  - Skill Match
  - Section Coverage
  - Formatting Quality
  - Keyword Match
- Get a semantic similarity percentage showing how well your resume matches the job description.
- Extract and compare key skills from your resume and the job posting.
- User-friendly interface powered by Streamlit.

---

## How It Works

1. **Upload Resume**: Upload your resume in PDF format.
2. **Paste Job Description**: Copy and paste the job description for the role you want to apply for.
3. **Analyze**: The app extracts text from your resume, compares it with the job description, and calculates:
    - ATS score based on keywords, sections, formatting, and skills.
    - Semantic similarity score using natural language processing techniques.
4. **Results**: View your score, matched skills, and personalized recommendations.

---

## Technologies Used

- **Python** with libraries such as:
  - `streamlit` for the web interface
  - `PyMuPDF (fitz)` for PDF text extraction
  - NLP libraries for semantic similarity (e.g., `sentence-transformers` or `sklearn`)
- Deployed on **Streamlit Cloud**

---

## Installation (For Local Use)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

##2.Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

##3.Install dependencies:
```bash
pip install -r requirements.txt
```
##4.Run the app locally:
```bash
streamlit run app.py
```

## Usage 
-Upload your PDF resume.

-Paste the job description in the text box.

-Click analyze and wait for the scores.

-Use the feedback to improve your resume and increase your chances of landing your dream job!

## Contributing

----Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.-----
