from flask import Flask, render_template, request, flash, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random value in a production environment

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laxmi103",
    database="user_registration_ques4"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('userId')
        mobile_number = request.form.get('mobileNumber')
        password = request.form.get('userPassword')

        # Perform user registration and database insertion
        try:
            query = "INSERT INTO usersques4 (user_id, mobile_number, password) VALUES (%s, %s, %s)"
            values = (user_id, mobile_number, password)
            cursor.execute(query, values)
            db.commit()

            flash('Registration successful!', 'success')  # Flash success message
            return redirect(url_for('welcome'))
        except mysql.connector.Error as err:
            db.rollback()
            flash(f'Registration failed: {err}', 'danger')  # Flash error message

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userId')
        password = request.form.get('userPassword')

        # Check user credentials against the database
        query = "SELECT * FROM usersques4 WHERE user_id = %s AND password = %s"
        cursor.execute(query, (user_id, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]  # Store user ID in session
            flash('Login successful!', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Login failed. Invalid credentials.', 'danger')

    return render_template('login.html')



@app.route('/welcome')
def welcome():
    if 'user_id' in session:
        return render_template('welcome.html')
    else:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
