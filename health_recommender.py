def get_recommendations(lab_values):
    recommendations = []

    if lab_values.get("blood_pressure") and lab_values["blood_pressure"] > 140:
        recommendations.append("High Blood Pressure: Consider consulting a cardiologist.")

    if lab_values.get("glucose") and lab_values["glucose"] > 125:
        recommendations.append("High Blood Sugar: Risk of Diabetes. Monitor diet and exercise.")

    if lab_values.get("hemoglobin") and lab_values["hemoglobin"] < 12:
        recommendations.append("Low Hemoglobin: You may be anemic. Include iron-rich foods.")

    if lab_values.get("cholesterol") and lab_values["cholesterol"] > 200:
        recommendations.append("High Cholesterol: Reduce oily food. Daily walking advised.")

    if not recommendations:
        recommendations.append("All lab values are within normal range. Keep up the healthy habits!")

    return recommendations


if __name__ == "__main__":
    sample_input = {
        "blood_pressure": 145,
        "glucose": 130,
        "hemoglobin": 11.5,
        "cholesterol": 220
    }

    for rec in get_recommendations(sample_input):
        print("-", rec)