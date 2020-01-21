from app import app
from flask import render_template
from flask_security import login_required

@app.route('/')
@login_required
def hello_world():
    return render_template('index.html')

