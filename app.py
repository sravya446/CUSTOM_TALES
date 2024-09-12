from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    age = request.form.get('age')

    # Ensure the path to mad_libs.py is correct
    mad_libs_path = os.path.join(os.getcwd(), 'mad_libs.py')

    # Launch the Tkinter application
    subprocess.Popen(["python", mad_libs_path])

    # Redirect to the confirmation page
    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
