import csv
from fpdf import FPDF

# Step 1: Setup Environment (CSV File Path)
CSV_FILE = "students.csv"
PDF_FILE = "students_report.pdf"


# Step 2: Store Student Information into a CSV File
def store_student_info():
    print("Enter student details to save into the CSV file.")
    students = []
    while True:
        student_id = input("Student ID: ").strip()
        name = input("Name: ").strip()
        roll = input("Roll: ").strip()
        semester = input("Semester: ").strip()
        shift = input("Shift: ").strip()
        department = input("Department: ").strip()
        dob = input("Date of Birth (YYYY-MM-DD): ").strip()
        phone = input("Phone No: ").strip()

        students.append([student_id, name, roll, semester, shift, department, dob, phone])

        more = input("Add another student? (yes/no): ").strip().lower()
        if more != "yes":
            break

    # Save to CSV
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student_ID", "Name", "Roll", "Semester", "Shift", "Department", "Date_of_Birth", "Phone_No"])
        writer.writerows(students)
    print(f"Student information saved to {CSV_FILE}")


# Step 3: Generate PDF Report from CSV
def generate_pdf_report():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add Title
    pdf.set_font("Arial", size=16, style="B")
    pdf.cell(200, 10, txt="Student Report", ln=True, align="C")
    pdf.ln(10)

    # Add Table Header
    pdf.set_font("Arial", size=12, style="B")
    headers = ["Student ID", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone No"]
    for header in headers:
        pdf.cell(25, 10, header, border=1, align="C")
    pdf.ln()

    # Add Table Rows
    pdf.set_font("Arial", size=10)
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                for cell in row:
                    pdf.cell(25, 10, cell, border=1, align="C")
                pdf.ln()
    except FileNotFoundError:
        print(f"Error: The file {CSV_FILE} does not exist. Please store data first.")

    # Save PDF
    pdf.output(PDF_FILE)
    print(f"PDF report generated: {PDF_FILE}")


# Main Function
def main():
    while True:
        print("\nOptions:")
        print("1. Store student information into CSV")
        print("2. Generate PDF report")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            store_student_info()
        elif choice == "2":
            generate_pdf_report()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
