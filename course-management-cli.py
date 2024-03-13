import sqlite3

# Setup the db -> Creating a connection to a db class instance => instanciate the database that is going to be used by application.

# A method within a class that will allow use to connect to the db.

# -> create the db 
# -> create the table(s)

class CourseManagementSystem:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                instructor TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                email TEXT UNIQUE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registrations (
                student_id INTEGER,
                course_id INTEGER, 
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id),
                UNIQUE(student_id, course_id)
            )
        ''')
        
        self.conn.commit()

    def add_course(self, name, instructor):

        if not name or not instructor:
            print("Error: Name and Instructor are required!")

        try: 
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO courses (name, instructor) VALUES (?, ?)", (name, instructor))
            self.conn.commit()
            print("Course Added Successfully")

        except sqlite3.IntegrityError:
            print(f"Error: Course {name} already exists!") 

    def add_student(self, first_name, last_name, email):

        if not first_name or not last_name or not email: 
            print("Error: First Name, Last Name and email are required!")
        
        try: 
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
            self.conn.commit()
            print("Student Added Successfully")
        
        except sqlite3.IntegrityError:
            print(f"Error: Student {first_name} {last_name} already exists!")

    def register_student_to_course(self, student_id, course_id):
        try: 

            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO registrations (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
            self.conn.commit()
            print("Student successfully added to this course")
        except sqlite3.IntegrityError: 
            print("Student is already added to this course")

    def get_all_courses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()

    def get_all_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

    def get_students_in_a_course(self, course_id):
       cursor = self.conn.cursor()
       cursor.execute("SELECT * FROM students INNER JOIN registrations ON students.id = registrations.student_id WHERE registrations.course_id = ? ", (course_id,))
       return cursor.fetchall()

if __name__ == '__main__':

    moringa_course_management = CourseManagementSystem("moringa_course_manager.db")

    # # Add some course 
    # moringa_course_management.add_course("Software Development", "Abel Kipkorir")
    # moringa_course_management.add_course("Character Development", "Clare Oparo")

    # # Add students
    # moringa_course_management.add_student("John", "Kimani", "johnkimani@gmail.com")
    # moringa_course_management.add_student("Naomi", "Lagat", "naomilagat@gmail.com")
    # moringa_course_management.add_student("Mariam", "Senzia", "mariam@gmail.com")
    # moringa_course_management.add_student("Dennis", "Kioko", "dennis@gmail.com")
    # moringa_course_management.add_student("Cynthia", "Chepkemoi", "cynthia@gmail.com")

    # # Register students to a course 
    # moringa_course_management.register_student_to_course(1, 2)
    # moringa_course_management.register_student_to_course(2, 2)
    # moringa_course_management.register_student_to_course(5, 2)
    # moringa_course_management.register_student_to_course(7, 1)
    # moringa_course_management.register_student_to_course(8, 2)

    # GET a list of courses and students 
    # print("********LIST OF COURSES*******")
    # print(moringa_course_management.get_all_courses())

    # print("********LIST OF STUDENTS******")
    # print(moringa_course_management.get_all_students())

    print("********LIST OF STUDENTS IN A SPECIFIC COURSE******")
    print(moringa_course_management.get_students_in_a_course(2))


    # HOW CAN WE DEAL WITH DATA DISCREPANCY
    # DUPLICATE DATA 
    # MISSING COLUMN VALUES 
    # NON LOGICAL ASSIGNMENT OF VALUES TO COLUMNS WITHIN THE DB

    # handling exceptions using the try catch 
    # db schema management -> Data uniqueness and data validation



