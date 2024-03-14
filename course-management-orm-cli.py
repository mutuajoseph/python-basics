# create our model classes 
# create the course management class 
# use the models created to perform all the necessary requirements/operations

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    instructor = Column(String, nullable=False)

    students = relationship('Student', secondary="registrations")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, unique=True, nullable=False)
    last_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)


class Registration(Base):
    __tablename__ = 'registrations'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True, nullable=False)

    __table_args__ = (
        UniqueConstraint('student_id', 'course_id', name='_student_course_uc'),
    )


class CourseManagementSystem: 

    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_course(self, name, instructor):
        if not name or not instructor:
            print("Error: Name and Instructor are required!")
        
        course = Course(name=name, instructor=instructor)

        try: 
            self.session.add(course)
            self.session.commit()
            print("Course Added Successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

    def add_student(self, first_name, last_name, email):
        if not first_name or not last_name or not email:
            print("Error: First Name, Last Name and email are required!")

        student = Student(first_name=first_name, last_name=last_name, email=email)
    
        try:
            self.session.add(student)
            self.session.commit()
            print("Student Added Successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')
    
    def register_student_to_course(self, student_id, course_id):

        registration = Registration(student_id=student_id, course_id=course_id)

        try:
            self.session.add(registration)
            self.session.commit()
            print("Student Successfully Added to a course")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')
    
    def get_all_courses(self):
        return self.session.query(Course).all()

    def get_all_students(self):
        return self.session.query(Student).all()

    def get_students_in_a_course(self, course_id):
        course = self.session.query(Course).filter_by(id=course_id).first()

        if course:
            return course.students
        else: 
            print("Course not found")
            return []


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

    # # # Register students to a course 
    # moringa_course_management.register_student_to_course(1, 2)
    # moringa_course_management.register_student_to_course(2, 2)
    # moringa_course_management.register_student_to_course(5, 2)


    # GET a list of courses and students 
    print("********LIST OF COURSES*******")
    course_list = moringa_course_management.get_all_courses()

    for course in course_list:
        print(course.name)

    # print("********LIST OF STUDENTS******")
    # print(moringa_course_management.get_all_students())

    # print("********LIST OF STUDENTS IN A SPECIFIC COURSE******")
    # print(moringa_course_management.get_students_in_a_course(2))
    