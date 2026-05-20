# Strategic Business Planning using Python
# Google Colab Ready Code

# Install required libraries
!pip install pandas matplotlib seaborn openpyxl --quiet

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: Create Business Dataset
# -------------------------------

data = {
    "Year": [2022, 2023, 2024, 2025, 2026],
    "Revenue": [50000, 65000, 72000, 85000, 98000],
    "Expenses": [30000, 35000, 40000, 47000, 52000],
    "Customers": [1000, 1300, 1600, 1900, 2300]
}

df = pd.DataFrame(data)

# -------------------------------
# STEP 2: Calculate Profit
# -------------------------------

df["Profit"] = df["Revenue"] - df["Expenses"]

# -------------------------------
# STEP 3: Strategic Analysis
# -------------------------------

print("\n===== STRATEGIC BUSINESS PLANNING REPORT =====\n")

print("Business Dataset:\n")
print(df)

print("\nAverage Revenue:", df["Revenue"].mean())
print("Average Profit:", df["Profit"].mean())
print("Maximum Revenue:", df["Revenue"].max())
print("Minimum Expenses:", df["Expenses"].min())

# -------------------------------
# STEP 4: SWOT Analysis
# -------------------------------

swot = {
    "Strengths": ["High customer growth", "Increasing revenue"],
    "Weaknesses": ["Rising expenses", "Market competition"],
    "Opportunities": ["Digital expansion", "New products"],
    "Threats": ["Economic slowdown", "Competitor pricing"]
}

print("\n===== SWOT ANALYSIS =====\n")

for key, value in swot.items():
    print(f"{key}:")
    for item in value:
        print("-", item)
    print()

# -------------------------------
# STEP 5: Visualization
# -------------------------------

plt.figure(figsize=(10,5))

plt.plot(df["Year"], df["Revenue"], marker='o', label="Revenue")
plt.plot(df["Year"], df["Expenses"], marker='o', label="Expenses")
plt.plot(df["Year"], df["Profit"], marker='o', label="Profit")

plt.title("Strategic Business Performance")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)

plt.show()

# -------------------------------
# STEP 6: Customer Growth Chart
# -------------------------------

plt.figure(figsize=(8,5))

sns.barplot(x=df["Year"], y=df["Customers"])

plt.title("Customer Growth Analysis")
plt.xlabel("Year")
plt.ylabel("Customers")

plt.show()

# -------------------------------
# STEP 7: Export Report
# -------------------------------

df.to_excel("Strategic_Business_Report.xlsx", index=False)

print("\nExcel report saved as Strategic_Business_Report.xlsx")
print("\nStrategic Business Planning Completed Successfully!")
