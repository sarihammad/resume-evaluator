from fpdf import FPDF

resume_text = """
John Doe
Data Analyst

Summary:
Detail-oriented analyst with experience in Python, SQL, and data visualization. Skilled at turning raw data into actionable insights.

Experience:
- Built automated dashboards in Excel and Tableau
- Analyzed customer behavior using Python and Pandas
- Created ETL pipelines using Airflow and PostgreSQL

Skills:
Python, SQL, Tableau, Excel, Pandas, Machine Learning
"""

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

for line in resume_text.strip().split('\n'):
    pdf.cell(200, 10, txt=line, ln=True)

pdf.output("resume_sample.pdf")
