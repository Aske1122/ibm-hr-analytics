import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv", sep=';')
sns.set_style("whitegrid")
sns.set_palette("muted")

# --- GRAF 1: Attrition per afdeling ---
fig, ax = plt.subplots(figsize=(8, 5))
dept_attrition = df.groupby("Department")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
).reset_index()
dept_attrition.columns = ["Department", "Attrition %"]
sns.barplot(data=dept_attrition, x="Department", y="Attrition %", ax=ax)
ax.set_title("Attrition-rate per afdeling", fontsize=14, pad=12)
ax.set_ylabel("Attrition %")
plt.tight_layout()
plt.savefig("outputs/01_attrition_by_department.png", dpi=150)
plt.close()
print("Gemt: 01_attrition_by_department.png")

# --- GRAF 2: Løn vs. attrition ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="Attrition", y="MonthlyIncome", ax=ax)
ax.set_title("Månedlig løn: forladt vs. ikke forladt", fontsize=14, pad=12)
ax.set_xlabel("Forladt virksomhed")
ax.set_ylabel("Månedlig løn (USD)")
plt.tight_layout()
plt.savefig("outputs/02_income_vs_attrition.png", dpi=150)
plt.close()
print("Gemt: 02_income_vs_attrition.png")

# --- GRAF 3: Overtime og attrition ---
fig, ax = plt.subplots(figsize=(6, 5))
overtime = df.groupby(["OverTime", "Attrition"]).size().unstack()
overtime.plot(kind="bar", ax=ax, rot=0)
ax.set_title("Overtime og attrition", fontsize=14, pad=12)
ax.set_xlabel("Arbejder overtime")
ax.set_ylabel("Antal medarbejdere")
ax.legend(title="Forladt")
plt.tight_layout()
plt.savefig("outputs/03_overtime_attrition.png", dpi=150)
plt.close()
print("Gemt: 03_overtime_attrition.png")

# --- GRAF 4: Alder fordeling ---
fig, ax = plt.subplots(figsize=(8, 5))
df[df["Attrition"] == "Yes"]["Age"].hist(ax=ax, alpha=0.6, label="Forladt", bins=20)
df[df["Attrition"] == "No"]["Age"].hist(ax=ax, alpha=0.6, label="Ikke forladt", bins=20)
ax.set_title("Aldersfordeling: forladt vs. ikke forladt", fontsize=14, pad=12)
ax.set_xlabel("Alder")
ax.set_ylabel("Antal")
ax.legend()
plt.tight_layout()
plt.savefig("outputs/04_age_distribution.png", dpi=150)
plt.close()
print("Gemt: 04_age_distribution.png")