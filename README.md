# 🩺 Health Lab Recommender System

This is a simple AI/ML project that gives health recommendations based on basic lab values. It is built as part of the Jayadhi Internship Assignment (AI/ML Intern - Recommendation System).

---

## 📌 Objective

To analyze user lab test data (e.g., blood pressure, glucose level, hemoglobin, cholesterol) and provide rule-based health recommendations.

---

## ⚙️ Technologies Used

- Python 3
- Rule-Based Logic
- Optional: Streamlit (for simple UI)

---

## 📥 Input Parameters

| Parameter       | Expected Type | Normal Range      |
|----------------|---------------|-------------------|
| Blood Pressure  | Integer       | < 140             |
| Glucose         | Integer       | < 125             |
| Hemoglobin      | Float         | ≥ 12              |
| Cholesterol     | Integer       | < 200             |

---

## 🧠 Sample Logic

- If blood pressure > 140 → Recommend checking with a cardiologist.
- If glucose > 125 → Suggest diabetes monitoring.
- If hemoglobin < 12 → Alert about anemia.
- If cholesterol > 200 → Advise diet and exercise.
- If all normal → Appreciate healthy habits.

---

## 🧪 Sample Output

Run:
```bash
python health_recommender.py
