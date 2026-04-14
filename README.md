# College-Placement-Predictor
I have created a project that is Placement Predictor that analyzes a student's academic profile and predicts placement probability, expected salary, and provides personalized improvement suggestions.
# 🎓 AI Placement Predictor

A machine learning web application that predicts a student's placement chances and expected salary package based on their academic and extracurricular profile.

---

## 📌 About The Project

This project uses a **Random Forest** machine learning model trained on real student placement data to predict:
- ✅ Probability of getting placed (in %)
- 💰 Expected salary package (in LPA)

It also gives a **personalized roadmap** suggesting what the student should improve to increase their placement chances.

---

## 🖥️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application UI |
| Scikit-learn | ML model training |
| Pandas | Data processing |
| Plotly | Interactive charts |
| Joblib | Saving and loading models |

---

## 📂 Project Structure

```
📦 project
 ┣ 📄 app.py                                        # Streamlit web app
 ┣ 📄 train.py                                      # Model training script
 ┣ 📄 student_placement_prediction_dataset_2026.csv # Dataset
 ┣ 📄 requirements.txt                              # Dependencies
 ┗ 📄 README.md                                     # Project documentation
```

---

## ⚙️ How To Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/your-username/ai-placement-predictor.git
cd ai-placement-predictor
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Train the model**
```bash
python train.py
```
> This will create a `models/` folder with the trained `.pkl` files.

**Step 4 — Run the app**
```bash
streamlit run app.py
```

Then open your browser and go to `http://localhost:8501`

---

## 📊 Input Features

| Feature | Description |
|---|---|
| CGPA | Academic score out of 10 |
| Internships | Number of internships completed |
| Projects | Number of projects built |
| Mock Interview Score | Score out of 10 |
| Backlogs | Number of backlogs |
| Skills Score | Skill level in Python, DSA, ML (0–10) |

---

## 📈 Output

- **Placement Probability** — percentage chance of getting placed
- **Expected Salary** — predicted salary in LPA (Lakhs Per Annum)
- **Placement Breakdown Chart** — visual bar chart of placed vs not placed probability
- **Personalized Roadmap** — suggestions to improve weak areas

---

## 🚀 Future Improvements

- [ ] User login and prediction history
- [ ] Deploy on Streamlit Cloud for public access
- [ ] Add company recommendation based on profile
- [ ] Improve model accuracy with larger dataset

---

## 👨‍💻 Author

**Your Name**
- GitHub: https://github.com/sanjanatak10
- LinkedIn: https://www.linkedin.com/in/sanjana-tak-dev

---

## 📃 License

This project is for educational purposes.
