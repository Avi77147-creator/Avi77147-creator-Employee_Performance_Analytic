
# 📈 Employee Performance Analytics

A data-driven tool for analyzing employee performance, identifying high and low performers, and assessing attrition risk. Built with Python and visualized using Power BI.

## 🔧 Features

- Performance trend analysis
- Department-wise comparisons
- Attrition risk identification

## 🧰 Tech Stack

- Python
- Pandas
- Power BI

## 🚀 Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Load and analyze data in Jupyter Notebook or Python script:
```python
from preprocess import load_data, clean_data
from analysis import performance_summary, attrition_risk_analysis, project_efficiency

df = load_data("employee_data.csv")
df = clean_data(df)

summary = performance_summary(df)
risks = attrition_risk_analysis(df)
efficiency = project_efficiency(df)
```

3. Visualize in Power BI using the cleaned CSV.

## 📊 Example Dataset

See `employee_data.csv` for sample data.
