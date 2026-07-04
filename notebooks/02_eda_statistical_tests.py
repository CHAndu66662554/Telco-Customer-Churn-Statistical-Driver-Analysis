import pandas as pd
from scipy.stats import chi2_contingency,ttest_ind

df=pd.read_csv("../data/telco_churn_clean.csv")
ALPHA=0.05

categorical_cols=[
    "gender","SeniorCitizen","Partner","Dependents","PhoneService",
    "MultipleLines","InternetService","OnlineSecurity","OnlineBackup",
    "DeviceProtection","TechSupport","StreamingTV","StreamingMovies",
    "Contract","PaperlessBilling","PaymentMethod"
]

print("="*70)
print("CHI-SQUARE TESTS: Categorical Features vs Churn")
print("="*70)

chi_results=[]
for col in categorical_cols:
    contingency=pd.crosstab(df[col],df["Churn"])
    chi2,p,dof,expected=chi2_contingency(contingency)
    significant="YES" if p<ALPHA else "no"
    chi_results.append({"feature":col,"chi2_stat":round(chi2,2),"p_value":round(p,5),"significant":significant})

chi_df=pd.DataFrame(chi_results).sort_values("p_value")
print(chi_df.to_string(index=False))

numeric_cols=["tenure","MonthlyCharges","TotalCharges"]

print("\n"+"="*70)
print("T-TESTS (Welch's): Numeric Features vs Churn")
print("="*70)

t_results=[]
for col in numeric_cols:
    churned=df[df["Churn"]==1][col]
    retained=df[df["Churn"]==0][col]
    t_stat,p=ttest_ind(churned,retained,equal_var=False)
    significant="YES" if p<ALPHA else "no"
    t_results.append({
        "feature":col,
        "mean_churned":round(churned.mean(),2),
        "mean_retained":round(retained.mean(),2),
        "t_stat":round(t_stat,2),
        "p_value":round(p,5),
        "significant":significant
    })

t_df=pd.DataFrame(t_results)
print(t_df.to_string(index=False))

chi_df.to_csv("../outputs/chi_square_results.csv",index=False)
t_df.to_csv("../outputs/ttest_results.csv",index=False)

print("\nSaved test results to /outputs")