import sqlite3
from tkinter import *
# ========================================================= 1st run =====================================================


# Database setup
def setup_database():
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor() # Create a cursor object to execute SQL commands.
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Function to save data
def save_data():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        conn = sqlite3.connect('student_data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, int(age)))
        conn.commit()
        conn.close()
        status_label.config(text="Data saved successfully!")
        name_entry.delete(0, END)
        age_entry.delete(0, END)
    else:
        status_label.config(text="Please enter both name and age.")

# Function to search data
def search_data():
    search_name = search_entry.get()
    if search_name:
        conn = sqlite3.connect('student_data.db')
        cursor = conn.cursor()  # Create a cursor object to execute SQL commands.
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + search_name + '%',))
        results = cursor.fetchall() # search all row
        conn.close()
        search_results.delete(1.0, END)  # Clear previous results
        if results:
            for row in results:
                search_results.insert(END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}\n") # Loop through the results and display each student's id, name, and age in the search_results widget.
        else:
            search_results.insert(END, "No results found.")
    else:
        status_label.config(text="Please enter a name to search.")

# GUI setup
root = Tk() # ========================================================= 1st run =====================================================
root.title("Student Management System")



# streated here 
# Input Form
Label(root, text="Enter Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Enter Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

save_button = Button(root, text="Save", command=save_data)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

# Search Form
Label(root, text="Search Name:").grid(row=3, column=0, padx=10, pady=5)
search_entry = Entry(root)
search_entry.grid(row=3, column=1, padx=10, pady=5)

search_button = Button(root, text="Search", command=search_data)
search_button.grid(row=4, column=0, columnspan=2, pady=10)

# Search Results
Label(root, text="Search Results:").grid(row=5, column=0, columnspan=2, pady=5)
search_results = Text(root, height=5, width=40)
search_results.grid(row=6, column=0, columnspan=2, pady=5)

# Status Label
status_label = Label(root, text="", fg="green")
status_label.grid(row=7, column=0, columnspan=2, pady=10)

# Initialize Database
setup_database()

# Run GUI
root.mainloop()  # ========================================================= 1st run =====================================================
