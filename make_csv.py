import pandas as pd

def create_student_csv():
    # Define student data
    data = {
        "Student_Id": [1, 2, 3],
        "Name": ["John Doe", "Jane Smith", "Alice Brown"],
        "Roll": [101, 102, 103],
        "Semester": ["Spring 2025", "Spring 2025", "Spring 2025"],
        "Shift": ["Morning", "Evening", "Morning"],
        "Department": ["CSE", "EEE", "ME"],
        "Date_of_Birth": ["2000-01-15", "2001-03-22", "1999-11-30"],
        "Phone_No": ["1234567890", "0987654321", "1122334455"]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save to a CSV file
    df.to_csv("students.csv", index=False)
    print("CSV file 'students.csv' created successfully.")

# Run this function to create the CSV file
create_student_csv()
