import pandas as pd
import sqlite3

df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv", sep=';')

# Gem data i SQLite database
conn = sqlite3.connect("data/hr.db")
df.to_sql("employees", conn, if_exists="replace", index=False)

print("=== 1. ATTRITION PER AFDELING ===")
q1 = """
    SELECT Department,
           COUNT(*) AS total,
           SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_company,
           ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_pct
    FROM employees
    GROUP BY Department
    ORDER BY attrition_pct DESC
"""
print(pd.read_sql_query(q1, conn))

print("\n=== 2. GENNEMSNITSLØN: FORLADT VS. IKKE FORLADT ===")
q2 = """
    SELECT Attrition,
           ROUND(AVG(MonthlyIncome), 0) AS avg_monthly_income,
           ROUND(AVG(Age), 1) AS avg_age,
           ROUND(AVG(YearsAtCompany), 1) AS avg_years
    FROM employees
    GROUP BY Attrition
"""
print(pd.read_sql_query(q2, conn))

print("\n=== 3. HVILKE JOBROLLER HAR HØJEST ATTRITION? ===")
q3 = """
    SELECT JobRole,
           COUNT(*) AS total,
           ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_pct
    FROM employees
    GROUP BY JobRole
    ORDER BY attrition_pct DESC
    LIMIT 5
"""
print(pd.read_sql_query(q3, conn))

print("\n=== 4. OVERTIME OG ATTRITION ===")
q4 = """
    SELECT OverTime,
           ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_pct
    FROM employees
    GROUP BY OverTime
"""
print(pd.read_sql_query(q4, conn))

conn.close()