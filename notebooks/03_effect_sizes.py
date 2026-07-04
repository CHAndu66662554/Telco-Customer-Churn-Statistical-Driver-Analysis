import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df=pd.read_csv("../data/telco_churn_clean.csv")

def cramers_v(col,target="Churn"):
    contingency=pd.crosstab(df[col],df[target])
    chi2,p,dof,expected=chi2_contingency(contingency)
    n=contingency.sum().sum()
    min_dim=min(contingency.shape)-1
    return np.sqrt(chi2/(n*min_dim))

categorical_cols=[
    "gender","SeniorCitizen","Partner","Dependents","PhoneService",
    "MultipleLines","InternetService","OnlineSecurity","OnlineBackup",
    "DeviceProtection","TechSupport","StreamingTV","StreamingMovies",
    "Contract","PaperlessBilling","PaymentMethod"
]

results=[]
for col in categorical_cols:
    v=cramers_v(col)
    if v<0.10:
        strength="negligible"
    elif v<0.30:
        strength="weak"
    elif v<0.50:
        strength="moderate"
    else:
        strength="strong"
    results.append({"feature":col,"cramers_v":round(v,3),"strength":strength})

results_df=pd.DataFrame(results).sort_values("cramers_v",ascending=False)
print(results_df.to_string(index=False))

results_df.to_csv("../outputs/effect_sizes.csv",index=False)
print("\nSaved to /outputs/effect_sizes.csv")