import pandas as pd
import numpy as np

df = pd.read_csv("../data/telco_churn_raw.csv")

print("Raw shape:", df.shape)
print("\nData types:\n", df.dtypes)


print("\nRows where TotalCharges is not a clean number:")
bad_rows = df[pd.to_numeric(df["TotalCharges"], errors="coerce").isna()]
print(bad_rows[["customerID", "tenure", "MonthlyCharges", "TotalCharges"]])

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

df.loc[df["tenure"] == 0, "TotalCharges"] = df.loc[df["tenure"] == 0, "TotalCharges"].fillna(0)

print("\nRemaining nulls after fix:", df["TotalCharges"].isna().sum())

cols_to_simplify = [
    "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies"
]
for col in cols_to_simplify:
    df[col] = df[col].replace({"No internet service": "No"})

df["MultipleLines"] = df["MultipleLines"].replace({"No phone service": "No"})

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df["SeniorCitizen"] = df["SeniorCitizen"].map({1: "Yes", 0: "No"}) 

dupes = df.duplicated(subset="customerID").sum()
print("\nDuplicate customerIDs:", dupes)

df.to_csv("../data/telco_churn_clean.csv", index=False)
print("\nSaved cleaned dataset. Final shape:", df.shape)
print("\nChurn rate: {:.1f}%".format(df["Churn"].mean() * 100))