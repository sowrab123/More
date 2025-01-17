from fpdf import FPDF
import pandas as pd

def generate_pdf_report(csv_file, output_pdf):
    # Load CSV data
    df = pd.read_csv(csv_file)

    # Initialize FPDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Student Information Report", ln=True, align="C")
    pdf.ln(10)

    # Add table headers
    pdf.set_font("Arial", size=12, style="B")
    headers = list(df.columns)
    for header in headers:
        pdf.cell(30, 10, header, border=1, align="C")
    pdf.ln()

    # Add table rows
    pdf.set_font("Arial", size=10)
    for index, row in df.iterrows():
        for value in row:
            pdf.cell(30, 10, str(value), border=1, align="C")
        pdf.ln()

    # Save PDF
    pdf.output(output_pdf)
    print(f"PDF report '{output_pdf}' generated successfully.")

# Run the function
generate_pdf_report("students.csv", "student_report.pdf")
