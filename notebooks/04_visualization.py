import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../data/telco_churn_clean.csv")

churn_by_contract=df.groupby("Contract")["Churn"].mean().sort_values(ascending=False)*100

fig,ax=plt.subplots(figsize=(7,5))
bars=ax.bar(churn_by_contract.index,churn_by_contract.values,color=["#d64545","#e8a33d","#4a90a4"])
ax.set_ylabel("Churn Rate (%)")
ax.set_title("Churn Rate by Contract Type\n(strongest driver, Cramer's V = 0.41)")
ax.set_ylim(0,50)

for bar in bars:
    height=bar.get_height()
    ax.annotate(f"{height:.1f}%",xy=(bar.get_x()+bar.get_width()/2,height),xytext=(0,5),textcoords="offset points",ha="center",fontweight="bold")

plt.tight_layout()
plt.savefig("../outputs/churn_by_contract.png",dpi=150)
print("Saved chart to ../outputs/churn_by_contract.png")
print("\n",churn_by_contract)