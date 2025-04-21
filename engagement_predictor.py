import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load your data
df = pd.read_csv("linkedin_posts.csv")

# Feature Engineering
features = ["word_count", "has_cta", "has_emoji"]
X = df[features]
y = df["likes"] + df["comments"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"Model accuracy (R²): {score:.2f}")

# Save the model
joblib.dump(model, "engagement_model.pkl")
