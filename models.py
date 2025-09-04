from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    major = db.Column(db.String(100))
    enrollment_date = db.Column(db.Date, nullable=False)
    graduation_date = db.Column(db.Date)
    gpa = db.Column(db.Float)
    
    def __repr__(self):
        return f'<Student {self.first_name} {self.last_name}>'