# Avi77147-creator-Employee_Performance_Analytic

📈 Employee Performance Analytics
A data-driven tool for analyzing employee performance, identifying high and low performers, and assessing attrition risk. Built with Python and visualized using Power BI.

🔧 Features
Performance trend analysis
Department-wise comparisons
Attrition risk identification
🧰 Tech Stack
Python
Pandas
Power BI
🚀 Getting Started
Install dependencies:
pip install -r requirements.txt
Load and analyze data in Jupyter Notebook or Python script:
from preprocess import load_data, clean_data
from analysis import performance_summary, attrition_risk_analysis, project_efficiency

df = load_data("employee_data.csv")
df = clean_data(df)

summary = performance_summary(df)
risks = attrition_risk_analysis(df)
efficiency = project_efficiency(df)
Visualize in Power BI using the cleaned CSV.
📊 Example Dataset
See employee_data.csv for sample data.
