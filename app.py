
# Then export/download the image as `logic_tree.png` and place it in your folder.

# ---

# ## ✅ 4. Optional UI File: `app.py`

# If you want to include UI with bonus points (optional), create `app.py` and paste this:

# ```python
import streamlit as st
from health_recommender import get_recommendations

st.title("🩺 Health Lab Recommender")

bp = st.number_input("Enter Blood Pressure:", min_value=0)
glucose = st.number_input("Enter Glucose Level:", min_value=0)
hb = st.number_input("Enter Hemoglobin:", min_value=0.0)
chol = st.number_input("Enter Cholesterol Level:", min_value=0)

if st.button("Get Health Recommendations"):
    values = {
        "blood_pressure": bp,
        "glucose": glucose,
        "hemoglobin": hb,
        "cholesterol": chol
    }
    results = get_recommendations(values)
    for r in results:
        st.success(r)
