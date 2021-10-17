import sqlite3

# Connect to database

connection = sqlite3.connect('courses.db')
cursor = connection.cursor()

# Create tables for planned and completed classes
cursor.execute("CREATE TABLE IF NOT EXISTS completed (year INT, semester TEXT, course_code TEXT, grade TEXT, credits INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS planned (year INT, semester TEXT, course_code TEXT, grade TEXT, credits INT)")

def get_course_code(cursor):
    cursor.execute("SELECT course_code FROM planned")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No courses in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Select course: "))
    return results[choice-1][0]


choice = None
while choice != "7":
    print("1: View completed courses ")
    print("2: View planned courses ")
    print("3: Add completed courses ")
    print("4: Add planned courses")
    print("5: Delete courses you have completed from your planned courses")
    print("6: Show total credits taken / planned ")
    print("7: Quit ")
    choice = input("> ")
    print()

    if choice == "1":
        # Display past courses and total courses completed
        cursor.execute("SELECT * FROM completed ORDER BY year ASC")
        print("{:>10}  {:>10}  {:>10} {:>10}  {:>10}".format("Year", "Semester", "Course Code", "Grade", "Credits"))
        for record in cursor.fetchall():
            print("{:>10} {:>10} {:>10} {:>10} {:>10}".format(record[0], record[1], record[2], record[3], record[4]))
        cursor.execute("SELECT COUNT(*) FROM completed")
        print("Classes taken: ", cursor.fetchall()[-1][-1])
    elif choice == "2":
        # Display planned courses and total courses planned
        cursor.execute("SELECT * FROM planned ORDER BY year ASC")
        print("{:>10}  {:>10}  {:>10} {:>10} {:>10}".format("Year", "Semester", "Course Code", "Grade", "Credits"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10} {:>10}  {:>10}".format(record[0], record[1], record[2], record[3], record[4]))
        cursor.execute("SELECT COUNT(*) FROM planned")
        print("Classes planned: ", cursor.fetchall()[-1][-1])
    elif choice == "3":
        # Update past courses
        year = input("Year: ")
        semester = input("Semester: ")
        course_code = input("Course code: ")
        grade = input("Grade: ")
        credits = int(input("Credits: "))
        values = (year, semester, course_code, grade, credits)
        cursor.execute("INSERT INTO completed VALUES (?,?,?,?,?)", values)
        connection.commit()
    elif choice == "4":
        # Add planned courses
        year = input("Year: ")
        semester = input("Semester: ")
        course_code = input("Course code: ")
        grade = input("Grade ('P' for planned courses): ")
        credits = int(input("Credits: "))
        values = (year, semester, course_code, grade, credits)
        cursor.execute("INSERT INTO planned VALUES (?,?,?,?,?)", values)
        connection.commit()
    elif choice == "5":
      # Delete completed courses from planned 
        course_code = get_course_code(cursor)
        if course_code == None:
            continue
        values = (str(course_code), )
        cursor.execute("DELETE FROM planned WHERE course_code = ?", values)
        connection.commit()
    elif choice == "6":
        # Display total credits taken and total credits planned
        cursor.execute("SELECT (SUM(credits)) FROM completed")
        print("Completed Credits:", cursor.fetchall()[0][0])
        cursor.execute("SELECT (SUM(credits)) FROM planned")
        print("Planned Credits:", cursor.fetchall()[0][0])
    print()


# Close the database connection
connection.close()



