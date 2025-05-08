
def performance_summary(df):
    return df.groupby('Department')['PerformanceRating'].agg(['mean', 'min', 'max', 'count'])

def attrition_risk_analysis(df):
    return df[df['AttritionRisk'] >= 0.7][['EmployeeID', 'Name', 'AttritionRisk']]

def project_efficiency(df):
    df['Efficiency'] = df['ProjectsCompleted'] / df['MonthlyHours']
    return df.sort_values(by='Efficiency', ascending=False)
