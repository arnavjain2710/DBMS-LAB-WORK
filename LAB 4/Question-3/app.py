from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random value in a production environment

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laxmi103",
    database="user_registration"
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('userId')
        mobile_number = request.form.get('mobileNumber')
        password = request.form.get('userPassword')

        # Perform user registration and database insertion
        try:
            query = "INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)"
            values = (user_id, mobile_number, password)
            cursor.execute(query, values)
            db.commit()

            flash('Registration successful!', 'success')  # Flash success message
        except mysql.connector.Error as err:
            db.rollback()
            flash(f'Registration failed: {err}', 'danger')  # Flash error message

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
