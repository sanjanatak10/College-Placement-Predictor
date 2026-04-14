import pandas as pd
import os
import joblib

# Load dataset
df = pd.read_csv("student_placement_prediction_dataset_2026.csv")

# Clean
df = df.dropna()

# ✅ ADD NEW FEATURES (if not present)
if "backlogs" not in df.columns:
    df["backlogs"] = 0

if "skills_score" not in df.columns:
    df["skills_score"] = (df["projects"] * 2 + df["internships"] * 3)

# Encode
df = pd.get_dummies(df, drop_first=True)

# Target
target_col = [col for col in df.columns if "placement_status" in col][0]

X = df.drop([target_col, 'salary_package_lpa'], axis=1)
y = df[target_col]

# Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ✅ Better model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced'
)

model.fit(X_train, y_train)

# Accuracy
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

# ================= SALARY =================
df_salary = df[df[target_col] == 1]

X_sal = df_salary[X.columns]
y_sal = df_salary['salary_package_lpa']

from sklearn.ensemble import RandomForestRegressor
model_salary = RandomForestRegressor(n_estimators=200)
model_salary.fit(X_sal, y_sal)

# Save
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/placement_model.pkl")
joblib.dump(model_salary, "models/salary_model.pkl")
joblib.dump(X.columns.tolist(), "models/features.pkl")

print("✅ Models saved!")