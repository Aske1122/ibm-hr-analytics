# HR Attrition Analysis

## Overview

This project analyzes employee attrition using the IBM HR Analytics dataset.
The goal is to identify patterns and factors associated with employees leaving the company.

## Tableau 

https://public.tableau.com/app/profile/aske.luther.hermansen/viz/Attrition_17770267285360/Dashboard1?publish=yes

## Dataset

The dataset contains information on 1470 employees and 35 variables, including:

* Demographics (age, gender)
* Job-related factors (department, role, income)
* Work conditions (overtime, travel frequency)

## Analysis

### Attrition by department

Sales has the highest attrition rate (~20.6%), followed by Human Resources and Research & Development.

### Income and attrition

Employees who leave the company tend to have lower monthly income on average.

### Overtime

Overtime is strongly associated with attrition. Employees working overtime leave at a significantly higher rate (~30%) compared to those who do not (~10%).

### Age distribution

Younger employees are more likely to leave compared to older employees.

## SQL Analysis

Data was also loaded into a SQLite database and analyzed using SQL queries. Example:

```sql
SELECT Department,
       COUNT(*) AS total,
       ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_pct
FROM employees
GROUP BY Department;
```

## Project Structure

```
ibm-hr-analytics/
├── data/
├── scripts/
├── outputs/
├── requirements.txt
└── README.md
```

## How to run

```bash
git clone <repo>
cd ibm-hr-analytics

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python scripts/01_explore.py
python scripts/02_analysis.py
python scripts/03_visualizations.py
```

## Key findings

* Overtime is the strongest indicator of attrition
* Lower income is associated with higher attrition
* Sales has the highest attrition rate
* Younger employees are more likely to leave

## Conclusion

The analysis suggests that workload and compensation are key factors in employee retention. Reducing overtime and improving salary conditions may help reduce attrition.
