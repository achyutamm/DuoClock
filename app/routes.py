from flask import current_app as app
from flask import render_template, jsonify
from datetime import datetime
import pytz

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def time():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    est_timezone = pytz.timezone('US/Eastern')
    
    # Get current time in IST and EST with respective dates
    ist_now = datetime.now(ist_timezone)
    est_now = datetime.now(est_timezone)

    ist_time = ist_now.strftime('%I:%M:%S %p')
    ist_date = ist_now.strftime('%A, %d %B, %Y')

    est_time = est_now.strftime('%I:%M:%S %p')
    est_date = est_now.strftime('%A, %d %B, %Y')
    
    return jsonify(ist_time=ist_time, ist_date=ist_date, est_time=est_time, est_date=est_date)
