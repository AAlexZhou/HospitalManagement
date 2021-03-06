# core/views.py

from flask import flash, request, Blueprint, Response, abort, render_template, redirect, jsonify
# from flask_login import LoginManager, login_user, logout_user, login_required
# from collections import defaultdict
# import traceback
from HM.database import *

core = Blueprint('core',__name__)

# Initialisation
database().__init__

@core.route('/')
def index():
    # MORE TO COME!
    return render_template('index.html')

@core.route('/login', methods=['GET','POST'])
def login():
    error = None
    if (request.method == "POST"):
        doctor_id = request.form["doctor_id"]
        password = request.form["password"]

        is_logged_in = database().login(doctor_id, password)
        if (is_logged_in):
            return render_template('dashboard.html')
        else:
            error = "Invalid credentials"
            return render_template('login.html', error=error)

        
    else:
        return render_template('login.html', error=error)
