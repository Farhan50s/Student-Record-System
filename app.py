from flask import Flask ,render_template, request, redirect, url_for, flash
from models import db, Student
from datetime import datetime
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students')
def students():
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get form data
        student_data = {
            'student_id': request.form['student_id'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'date_of_birth': datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date(),
            'major': request.form['major'],
            'enrollment_date': datetime.strptime(request.form['enrollment_date'], '%Y-%m-%d').date(),
            'graduation_date': datetime.strptime(request.form['graduation_date'], '%Y-%m-%d').date() if request.form['graduation_date'] else None,
            'gpa': float(request.form['gpa']) if request.form['gpa'] else None
        }
        
        # Create new student
        new_student = Student(**student_data)
        
        try:
            db.session.add(new_student)
            db.session.commit()
            flash('Student added successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding student: {str(e)}', 'danger')
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = Student.query.get_or_404(id)
    
    if request.method == 'POST':
        # Update student data
        student.student_id = request.form['student_id']
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        student.email = request.form['email']
        student.date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
        student.major = request.form['major']
        student.enrollment_date = datetime.strptime(request.form['enrollment_date'], '%Y-%m-%d').date()
        student.graduation_date = datetime.strptime(request.form['graduation_date'], '%Y-%m-%d').date() if request.form['graduation_date'] else None
        student.gpa = float(request.form['gpa']) if request.form['gpa'] else None
        
        try:
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating student: {str(e)}', 'danger')
    return render_template('edit.html', student=student)

@app.route('/view/<int:id>')
def view(id):
    student = Student.query.get_or_404(id)
    return render_template('view.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get_or_404(id)
    
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting student: {str(e)}', 'danger')
    
    return redirect(url_for('students'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)