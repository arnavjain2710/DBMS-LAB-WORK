from flask import Flask, render_template, request, flash, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random value in a production environment

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userId')
        user_password = request.form.get('userPassword')

        # Perform user registration logic here (e.g., save to a database)
        # Replace the print statement with your actual registration code
        print(f'Registering User: UserID: {user_id}, Password: {user_password}')

        # Simulate a successful registration
        # In a real application, you would perform actual registration logic here
        # For demonstration purposes, we're just returning a JSON response.
        if user_id:
            flash('Registration successful!', 'success')
            return jsonify({'message': 'success', 'username': user_id})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
