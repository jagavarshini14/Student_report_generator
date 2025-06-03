import pandas as pd
from fpdf import FPDF

# Step 1: Read CSV
df = pd.read_csv("student_marks.csv")

# Step 2: Analyze data
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)
df["Result"] = df[["Maths", "Science", "English"]].apply(lambda x: "Pass" if all(i >= 35 for i in x) else "Fail", axis=1)

overall_avg = df["Average"].mean()
pass_count = df[df["Result"] == "Pass"].shape[0]
fail_count = df[df["Result"] == "Fail"].shape[0]

# Step 3: Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')
pdf.ln(10)

# Summary
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=f"Overall Average: {overall_avg:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Total Passed: {pass_count}", ln=True)
pdf.cell(200, 10, txt=f"Total Failed: {fail_count}", ln=True)
pdf.ln(10)

# Table header
pdf.set_font("Arial", size=11)
pdf.cell(40, 10, "Name", 1)
pdf.cell(25, 10, "Maths", 1)
pdf.cell(25, 10, "Science", 1)
pdf.cell(25, 10, "English", 1)
pdf.cell(25, 10, "Average", 1)
pdf.cell(25, 10, "Result", 1)
pdf.ln()

# Table rows
for index, row in df.iterrows():
    pdf.cell(40, 10, row["Name"], 1)
    pdf.cell(25, 10, str(row["Maths"]), 1)
    pdf.cell(25, 10, str(row["Science"]), 1)
    pdf.cell(25, 10, str(row["English"]), 1)
    pdf.cell(25, 10, f"{row['Average']:.2f}", 1)
    pdf.cell(25, 10, row["Result"], 1)
    pdf.ln()

pdf.output("sample_student_report.pdf")
print("Report generated!")