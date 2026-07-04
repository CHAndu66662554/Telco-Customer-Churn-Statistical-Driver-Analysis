# Telco Customer Churn: Statistical Driver Analysis

## Overview

Customer churn is one of the biggest challenges for subscription-based businesses. Instead of relying only on visualizations or correlations, this project combines statistical hypothesis testing with business intelligence to identify which customer attributes are genuinely associated with churn and which factors are important enough to prioritize.

The project analyzes **7,043 telecom customers** using Python for statistical analysis and Power BI for interactive visualization, demonstrating an end-to-end analytics workflow from data cleaning to business recommendations.

---

## Business Objective

This analysis aims to answer three key questions:

- Which customer and account characteristics are statistically associated with churn?
- Which of these factors have meaningful business impact rather than simply being statistically significant?
- What actions can the business take to reduce customer churn?

---

## Dataset

**Source:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The dataset contains:

- 7,043 customer records
- 21 customer and account attributes
- Demographic information
- Services subscribed
- Billing and contract information
- Overall churn rate: **26.5%**

---

## Project Workflow

### 1. Data Cleaning

- Fixed missing values in `TotalCharges` by identifying that they belonged to newly joined customers (`tenure = 0`) rather than removing records.
- Standardized service categories by replacing `"No internet service"` with `"No"` to avoid redundant categories during statistical testing.

---

### 2. Statistical Analysis

Performed hypothesis testing to determine whether customer attributes were significantly associated with churn.

**Categorical variables**
- Chi-Square Test of Independence

**Numerical variables**
- Welch's Independent Samples t-test

---

### 3. Effect Size Analysis

With more than 7,000 observations, many variables become statistically significant simply because of the large sample size.

To distinguish meaningful business drivers from statistical noise, **Cramer's V** was calculated for every categorical feature.

---

### 4. Data Visualization

Created visualizations in both **Python (Matplotlib)** and **Power BI** to communicate insights through an interactive dashboard.

---

# Key Findings

- **Contract type** was the strongest predictor of churn (Cramer's V = **0.41**).
  - Month-to-month: **42.7% churn**
  - One-year: **11.3% churn**
  - Two-year: **2.8% churn**

- Customers using **Fiber Optic Internet** and **Electronic Check** payment methods showed substantially higher churn rates.

- Customers who churned had:
  - Average tenure of **18 months**
  - Average monthly charges of **$74.44**

- Customers who stayed had:
  - Average tenure of **37.6 months**
  - Average monthly charges of **$61.27**

- Features such as **Gender**, **Phone Service**, **Streaming TV**, and **Multiple Lines** had either negligible or very weak practical impact despite some being statistically significant.

---

# Business Recommendations

Based on the statistical findings:

- Encourage month-to-month customers to move to longer-term contracts through targeted promotions.
- Investigate the high churn observed among Fiber Optic customers paying via Electronic Check to identify possible service or billing issues.
- Focus customer engagement during the first year, where churn risk is highest.

---

# Power BI Dashboard

The statistical analysis was complemented with an interactive Power BI dashboard for business users.

**Dashboard Preview**
<img width="1303" height="731" alt="Screenshot 2026-07-04 100432" src="https://github.com/user-attachments/assets/a8360f4c-5328-4de4-8cee-6bf3f805d374" />

The dashboard includes:

- Overall customer KPIs
- Churn rate by contract type
- Internet Service vs Payment Method heatmap
- Customer distribution by tenure
- Tenure vs Monthly Charges scatter plot
- Interactive slicers for Contract, Internet Service, and Senior Citizen status

---

# Sample Visualization

<p align="center">
  <img src="outputs/churn_by_contract.png" width="700">
</p>

---

# Project Structure

```text
telco-churn-analysis/
│
├── data/
│   ├── telco_churn_raw.csv
│   └── telco_churn_clean.csv
│
├── notebooks/
│   ├── 01_data_cleaning.py
│   ├── 02_eda_statistical_tests.py
│   ├── 03_effect_sizes.py
│   └── 04_visualization.py
│
├── outputs/
│   ├── chi_square_results.csv
│   ├── ttest_results.csv
│   ├── effect_sizes.csv
│   ├── churn_by_contract.png
│   └── power_bi_dashboard.png
│
├── Dashboard_telco-churn-analysis.pbix
│
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Power BI
- DAX
- Power Query

---

# Results

This project demonstrates how statistical testing and business intelligence can be combined to move beyond descriptive analytics. Rather than identifying variables that are merely correlated with churn, the analysis highlights the factors that have the strongest practical impact, providing actionable recommendations for customer retention strategies.

---
